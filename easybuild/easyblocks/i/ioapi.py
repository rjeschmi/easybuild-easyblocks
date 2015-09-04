

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

    
