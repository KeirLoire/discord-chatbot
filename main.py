import configparser
from classes.discord import Client
from classes.openai import Model

def main():
    # Get configuration values
    config = configparser.RawConfigParser()
    config.read('config.ini')

    # Configure OpenAI model
    Model.set_api_key = config['openai']['api_key']

    # Configure Discord Bot Client
    client = Client()
    client.set_prefix(config['discord']['prefix'])

    # Start Discord Bot Client
    client.run(config['discord']['api_key'])

if __name__ == "__main__":
    main()