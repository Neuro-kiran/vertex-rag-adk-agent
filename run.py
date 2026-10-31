import asyncio
import sys

from google.adk.runners import InMemoryRunner
from google.genai import types

from agent import root_agent


async def main(question: str) -> None:
    runner = InMemoryRunner(agent=root_agent, app_name="app")
    session = await runner.session_service.create_session(app_name="app", user_id="user")
    msg = types.Content(role="user", parts=[types.Part(text=question)])
    async for event in runner.run_async(user_id="user", session_id=session.id, new_message=msg):
        if event.is_final_response() and event.content and event.content.parts:
            print(event.content.parts[0].text)


if __name__ == "__main__":
    asyncio.run(main(" ".join(sys.argv[1:]) or "Hello"))
