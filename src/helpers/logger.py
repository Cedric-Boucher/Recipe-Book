import os
import datetime
import zipfile

class Logger():
    """A log file.
    Messages can be appended to it using log method.
    Messages are automatically timestamped.
    Log file is automatically added to a zip archive once it is too large.
    """
    def __init__(self, log_file_path: str):
        self.__MAX_FILESIZE: int = 10 * 1024 * 1024 # 10MB
        self.__log_file_path: str = os.path.abspath(log_file_path)
        self.__create_log_file_if_nonexistant()

    def __create_log_file_if_nonexistant(self) -> None:
        """Will check if the log file exists.
        If it doesn't exist, creates it (and any necessary folders).
        """
        if (not os.path.exists(self.__log_file_path)):
            path = os.path.dirname(self.__log_file_path)
            if (not os.path.exists(path)):
                os.makedirs(path)
            with open(self.__log_file_path, "x"):
                pass # write nothing, just create file
            assert (os.path.exists(self.__log_file_path) and os.path.isfile(self.__log_file_path)), "log file didn't exist and couldn't be created"

    def __is_file_too_large(self) -> bool:
        """checks if file is larger than maximum filesize defined

        Returns:
            bool: True if file is larger, False otherwise
        """
        try:
            filesize: int = os.path.getsize(self.__log_file_path)
        except:
            filesize: int = 0
        return filesize > self.__MAX_FILESIZE

    def __archive_file(self) -> None:
        """saves space on drive by adding current log file to zip archive.
        log files are timestamped in their filename when added to archive.
        this means that logs are stored in dated chunks for easy retrieval.
        """
        zip_file_path: str = ".".join(self.__log_file_path.split(".")[:-1])+".zip" # same as log file but change extension to zip
        archive_filename: str = str(datetime.datetime.now())+" "+os.path.basename(self.__log_file_path) # rename by adding datetime to have zipped logs as dated chunks
        self.__create_log_file_if_nonexistant()
        try:
            zip_file: zipfile.ZipFile = zipfile.ZipFile(zip_file_path, "a", zipfile.ZIP_LZMA, True)
            with zip_file as zip_file_writer:
                zip_file_writer.write(self.__log_file_path, archive_filename)
            with open(self.__log_file_path, "w"):
                pass # write nothing, just delete contents of the file
        except:
            self.log("Failed to archive log file")

    def log(self, message: str) -> None:
        """appends message to log file.
        automatically adds current datetime.
        automatically appends log to zip file if it is too large.

        Args:
            message (str): message to add to the end of the file (\\n is added after message)
        """
        self.__create_log_file_if_nonexistant()
        with open(self.__log_file_path, "a") as file:
            file.write(str(datetime.datetime.now())+": "+str(message)+"\n")

        file_is_too_large: bool = self.__is_file_too_large()
        if file_is_too_large:
            self.__archive_file()
