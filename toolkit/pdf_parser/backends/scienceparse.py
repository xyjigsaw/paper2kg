import os
import shutil
import logging
import tempfile
import subprocess as sp

from . import Backend


class ScienceParse(Backend):
    def __init__(self):
        super(ScienceParse, self).__init__()
        self.logger = logging.getLogger('pdf_parser.backend.scienceparse')

        file_dir = os.path.dirname(__file__)
        self.jar = os.path.join(file_dir, '..', 'jar', 'science-parse-cli-2.0.3.jar')

        self.typ2service = {
            'text': 'text',
        }

        self.health = None
        self._check_java()

    def _check_java(self):
        cmd = ['java', '-version']
        try:
            sp.run(cmd, stdout=sp.DEVNULL, stderr=sp.DEVNULL, check=True)
            self.health = True
        except Exception:
            self.health = False
            self.logger.error('No java in your environment.')

    @staticmethod
    def _move_result_from_tmp_to_output(tmp_dir, output_dir):
        for name in os.listdir(tmp_dir):
            prefix, ext = os.path.splitext(name)
            prefix = os.path.splitext(prefix)[0]
            new_name = prefix + '.scienceparse.json'
            shutil.move(os.path.join(tmp_dir, name), os.path.join(output_dir, new_name))

    def _process_pdf(self, input_file, output_dir, service, **kwargs):
        if not self.health:
            return 0

        with tempfile.TemporaryDirectory() as dirname:
            cmd = ['java', '-Xmx16g', '-jar', self.jar, '-o', dirname, input_file]
            sp.run(cmd, stdout=sp.DEVNULL, stderr=sp.DEVNULL)
            self._move_result_from_tmp_to_output(dirname, output_dir)
        return 1

    def _process_dir(self, input_dir, output_dir, service, n_threads=0, **kwargs):
        if not self.health:
            return 0

        with tempfile.TemporaryDirectory() as dirname:
            cmd = ['java', '-Xmx16g', '-jar', self.jar, '-o', dirname, input_dir]
            sp.run(cmd, stdout=sp.DEVNULL, stderr=sp.DEVNULL)
            self._move_result_from_tmp_to_output(dirname, output_dir)
        return sum(file[-4:] == '.pdf' for file in os.listdir(input_dir))

    # def parse(self, typ, input_path, output_dir, n_threads=0, **kwargs):
    #     typ2service = {
    #         'text': 'text',
    #     }
    #
    #     if typ not in typ2service:
    #         self.logger.error(f'Backend {self.__name__} could not parse for type "{typ}".')
    #         return 0
    #     service = typ2service[typ]
    #
    #     if os.path.isfile(input_path):
    #         return self._process_pdf(input_path, output_dir, service)
    #     else:
    #         return self._process_dir(input_path, output_dir, service, n_threads)
