import click
import json

@click.command()
@click.option('--file',help = 'specify a file to save')
@click.option('--format',default = 'dict',help = 'specify the format to save the parsed data in')
@click.option('--convert',default = 'y', help = 'convert to other format or not')
def actions(file,format,convert):
	df = open(file)
	dict = {}
	if format == 'dict':
		if convert == 'y':
			dict = json.loads(df.read())

	else:
		print("not aware of other formats")
	print(dict)


if __name__ == '__main__':
	actions()



