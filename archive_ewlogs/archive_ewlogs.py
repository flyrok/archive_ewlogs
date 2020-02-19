#!/usr/bin/env python3

'''
Archive earthworm log files in to yyyy-jjj directories

'''

from pathlib import Path
from datetime import datetime as dt
import argparse
import sys
import types

progname='archive_ewlogs';
__version_info__ = ('2019','12','01','0.02')
__version__ = '-'.join(__version_info__)


def archive_logs(inlogs,oroot,dryrun,debug):
    now=dt.now().strftime("%Y%m%d")
    for i in inlogs:
        j=str(i).split('_')
        ymd=j[-1].split('.')[0]
        if ymd == now:

            if (debug >1 ): print(f"{str(i)} is still active, not archiving (dryrun=={dryrun})")
            next
        else:
            try:
                file_date=dt.strptime(ymd,"%Y%m%d")
                year=file_date.strftime("%Y")
                jday=file_date.strftime("%j")
                p=oroot / str(year) / str(jday)
                mvf=Path(i).absolute()
                if not p.exists():
                    if (debug > 1): print(f"Need to make dir {str(p)} (dryrun=={dryrun})")
                    if not dryrun: # actually doit
                        p.mkdir(parents=True, exist_ok=True)
                if (debug > 1): print(f"Moving {str(mvf)} to {str(p)} (dryrun=={dryrun})")

                if not dryrun: # actually do it
                    mvf.rename(p / mvf.name)
            except Exception as e:
                print(f"Problem with {str(mvf)} ... {e}")

def main():
    logdir_default=f"{str(Path.home())}/ew_working/log/"
    outdir_default=f"{str(Path.home())}/ew_working/log/"
    parser = argparse.ArgumentParser(prog=progname,
        formatter_class=CustomFormatter,
        description=f'''Archive Earthworm Log files in yyyy/jjj directories 
        inlogdir default ({logdir_default})
        outroot default  ({logdir_default})
            '''
        )

    parser.add_argument("-i","--inlogdir", type=str, default=logdir_default,
        required=False, help="Location of log files to archive. Files show match pattern inlogdir/*.log")

    parser.add_argument("-o","--outroot", type=str, default=outdir_default,
        required=False, help="Archive root directory. Files will be moved to outroot/yyyy/jjj")

    parser.add_argument("-n", "--dryrun", action='store_false',default=True,
        required=False, help="Set this to actually do something. Defaults to dryrun with verbositity turned on")

    parser.add_argument("-v", "--verbose", action="count",default=0,
        help="increase spewage")

    parser.add_argument('--version', action='version',
        version='%(prog)s {version}'.format(version=__version__))

    args = parser.parse_args()
    iroot=Path(args.inlogdir)
    oroot=Path(args.outroot)
    debug=args.verbose
    dryrun=args.dryrun
    if not iroot.is_dir():
        print(args.inlogdir,"doesn't exist")
        sys.exit(0)
    if not oroot.is_dir():
        print(args.outroot,"doesn't exist")
        sys.exit(0)
   
    if dryrun: # if 
        debug=2    
        print(f"In dry-run mode, set --dryrun to turn off. Debug set to {debug}")
    inlogs=Path(iroot).glob('*.log')
    archive_logs(inlogs,oroot,dryrun,debug)


class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter):
    '''
    re-class ArgDefaults formatter to also print things pretty. Helps printing out the config file example
    '''
    def _get_help_string(self, action):
        help = action.help
        if '%(default)' not in action.help:
            if action.default is not argparse.SUPPRESS:
                defaulting_nargs = [argparse.OPTIONAL, argparse.ZERO_OR_MORE]
                if action.option_strings or action.nargs in defaulting_nargs:
                    if type(action.default) == type(sys.stdin):
                        print( action.default.name)
                        help += ' (default: ' + str(action.default.name) + ')'
                    else:
                        help += ' (default: %(default)s)'
        return help


if __name__ == '__main__':
    main()



