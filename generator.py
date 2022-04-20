from jinja2 import Template
import click


def generate_job(number):
    template = open("templates/template.jinja2").read()
    j2_template = Template(template)
    return j2_template.render({"number": number})
    
    
@click.command()
@click.argument('number', default=5)
def jobs(number):
    """Generates a numbef of jobs"""
    for i in range(number):
        click.echo(generate_job(i))
        
        

        
if __name__ == '__main__':
    jobs()
