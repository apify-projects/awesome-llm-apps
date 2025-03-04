"""This module defines the main entry point for the Apify Actor.

Feel free to modify this file to suit your specific needs.

To build Apify Actors, utilize the Apify SDK toolkit, read more at the official documentation:
https://docs.apify.com/sdk/python
"""

from apify import Actor

from src import ai_scrapper_func

async def main() -> None:
    """Main entry point for the Apify Actor.

    This coroutine is executed using `asyncio.run()`, so it must remain an asynchronous function for proper execution.
    Asynchronous execution is required for communication with Apify platform, and it also enhances performance in
    the field of web scraping significantly.
    """
    async with Actor:
        Actor.log.info('Hello from the Actor!')
        # Write your code here

        actor_input = await Actor.get_input() or {}

        Actor.log.info('Running the ai scrapper...')

        result = await ai_scrapper_func(**actor_input)

        Actor.log.info(f'Result: {result}')
        await Actor.set_output(result)

        Actor.exit(status_message='Actor finished successfully!')