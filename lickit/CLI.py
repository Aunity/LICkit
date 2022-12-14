import os
import sys
import argparse

def GMXMMPBSA_cli():
    from lickit.tools import parse_GMXMMPBSA_RESULTS
    parser = argparse.ArgumentParser(description='Parse the GMXMMPBSA results')
    parser.add_argument('-i', dest='mmxsa', help='mmxsa file generated by the gmx_MMPBSA.', required=True)
    parser.add_argument('-o', dest='outdir', help='Output directory to save parsed csv file.', default='.')
    args = parser.parse_args()
    mmxsafile, outdir = args.mmxsa, args.outdir
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    parse_GMXMMPBSA_RESULTS(mmxsafile, outdir)

