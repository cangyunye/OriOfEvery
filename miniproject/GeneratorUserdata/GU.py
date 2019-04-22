# !/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import textwrap
from UserDataGenerator import UserDataGenerator


__description__ = textwrap.dedent('''\
			About the project you need to know
		 ---------------------------------------
			Designed for generate user data.
			Supplying which is absent from we need.
			Expansibility by configs.
			''')

__version__ = "GU.0.0.2"
parser = argparse.ArgumentParser(description=__description__, formatter_class=argparse.RawDescriptionHelpFormatter,
								 prog='UserDataGenerator', epilog="Nowhere to be seen.")
#argument:servnumber,region,cfgfile
parser.add_argument('servnumber', metavar='servnumber', type=str,
					help='The 11 integer for the servnumber.')

parser.add_argument('region', metavar='region', type=str,
					help='The region of servnumber.')

parser.add_argument('-c','--config', action='append',dest='cfg',nargs='+',
					help='Specific business config.')

#addtional info
parser.add_argument('-b','--brand', required=False, type=str,choices=['szx','SZX','gt','GT'],
					help='Brand like szx as BrandSzx or gt as BrandGotone.')
parser.add_argument('-a','--active', required=False, type=str,
					help='If this servnumber activated.')
parser.add_argument('-r','--route', required=False, type=str,
					help='If route info is exists.')
parser.add_argument('-e','--env', required=False, type=str,choices=['crm','CRM','test','TEST'],
					help='Environment like crm as or test.')

#add_help
parser.add_argument('-v','--version', help='version:%s' % (__version__))
parser.add_argument('-d','--debug',action='store_true',help='show about debug',default=False)


args = parser.parse_args()


def main():
	param = {
		'servnumber':args.servnumber if args.servnumber  else None,
		'mode':args.mode,
		'region':args.region if args.region  else None,
		'scfg':args.scfg if args.scfg  else None,
		'bcfg':args.bcfg if args.bcfg  else None,
		'brand':args.brand if args.brand  else None,
		'brand':args.brand if args.brand  else None,
		'active':args.active if args.active  else None,
		'nodeid':args.nodeid if args.nodeid  else None,
		'cfgfile':args.cfg if args.cfg  else 'GlobalSettings.ini'
	}
	print(param)
	g=UserDataGenerator(args.servnumber)
	g.process(**param)

if __name__ == "__main__":
	main()