

from easybuild.easyblocks.generic.configuremake import ConfigureMake
from easybuild.tools.run import run_cmd

class EB_ioapi(ConfigureMake):
    """
    Building ioapi using an older build system similar to HPL
    """

    def configure_step(self, subdir=None):
        basedir = self.cfg['start_dir']
        
        cmd = "make %(buildopts)s configure" %  {
            'buildopts': self.cfg['buildopts'],
        }
        (out, _) = run_cmd( cmd, log_all=True, simple=False)
        return out

    def build_step(self, verbose=False, path=None):
        """
        Start the actual build
        - typical: make -j X
        """

        paracmd = ''
        if self.cfg['parallel']:
            paracmd = "-j %s" % self.cfg['parallel']

        cmd = "%s make all %s %s" % (self.cfg['prebuildopts'], paracmd, self.cfg['buildopts'])

        (out, _) = run_cmd(cmd, path=path, log_all=True, simple=False, log_output=verbose)

        return out    
