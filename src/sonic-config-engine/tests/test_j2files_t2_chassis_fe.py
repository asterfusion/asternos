import filecmp
import os
import subprocess
import json
import shutil

from unittest import TestCase

class TestJ2FilesT2ChassisFe(TestCase):
    def setUp(self):
        self.test_dir = os.path.dirname(os.path.realpath(__file__))
        self.script_file = os.path.join(self.test_dir, '..', 'sonic-cfggen')
        self.t2_chassis_fe_minigraph = os.path.join(self.test_dir, 't2-chassis-fe-graph.xml')
        self.t2_chassis_fe_vni_minigraph = os.path.join(self.test_dir, 't2-chassis-fe-graph-vni.xml')
        self.t2_chassis_fe_pc_minigraph = os.path.join(self.test_dir, 't2-chassis-fe-graph-pc.xml')
        self.t2_chassis_fe_port_config = os.path.join(self.test_dir, 't2-chassis-fe-port-config.ini')
        self.output_file = os.path.join(self.test_dir, 'output')

    def tearDown(self):
        try:
            os.remove(self.output_file)
        except OSError:
            pass

    def run_script(self, argument):
        print 'CMD: sonic-cfggen ' + argument
        return subprocess.check_output(self.script_file + ' ' + argument, shell=True)

    def run_diff(self, file1, file2):
        return subprocess.check_output('diff -u {} {} || true'.format(file1, file2), shell=True)

    def run_case(self, minigraph, template, target):
        self.run_script(cmd)

        original_filename = os.path.join(self.test_dir, 'sample_output', target)
        r = filecmp.cmp(original_filename, self.output_file)
        diff_output = self.run_diff(original_filename, self.output_file) if not r else ""

        return r, "Diff:\n" + diff_output
