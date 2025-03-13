"""This module defines the main entry point for the Apify Actor.

Feel free to modify this file to suit your specific needs.

To build Apify Actors, utilize the Apify SDK toolkit, read more at the official documentation:
https://docs.apify.com/sdk/python
Also, see more about why Actors are cool and easy to use here:
https://whitepaper.actor/
"""

from apify import Actor

from src import ai_scrapper_func

import asyncio
from concurrent.futures import ThreadPoolExecutor

async def run_scraper_in_thread(kwargs):
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as executor:
        return await loop.run_in_executor(executor, lambda: ai_scrapper_func(**kwargs))

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

        result = await run_scraper_in_thread(actor_input)

        Actor.log.info(f'URL: {actor_input.get("url")}')
        Actor.log.info(f'Prompt: {actor_input.get("user_prompt")}')
        Actor.log.info(f'Result: {result.get('content')}')
        await Actor.push_data(result)

        await Actor.exit(status_message='Actor finished successfully!')