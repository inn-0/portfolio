### Motivation:   "Parsing JSON is going to go wrong" - ArjanCodes   PyCon Lithuania    2024.04.04 Thu 15h57m

### Title:    Structured Your LLM Output Using the "Instructor" Package

### TL;DR:   Try the "instructor" package   https://github.com/jxnl/instructor/

### Original Code Source:    https://python.useinstructor.com/examples/entity_resolution/?h=entity

### Learn:   https://www.wandb.courses/courses/steering-language-models

### Observability with Weights&Biases or LangServe    e.g.   https://python.useinstructor.com/blog/2024/02/18/seamless-support-with-langsmith/?h=langsmith#langsmith

### Author Contact:    innoswit+we@pm.me      linkedin.com/in/jg-0ch/

import json

import instructor
from devtools import pprint
from openai import OpenAI
from pydantic import BaseModel, Field
from rich.console import Console

with open("/mnt/c/tmp/.env", "r") as file:  # SECRETS FROM FILE
    API_KEY_OPENAI = json.load(file)["API_KEY_OPENAI"]


client = instructor.from_openai(OpenAI(api_key=API_KEY_OPENAI))


class Property(BaseModel):
    key: str = Field(..., description="maximum 120chars")
    value: str


class Entity(BaseModel):
    entity_title: str

    id: int = Field(
        ...,
        description="Unique identifier for the entity",
    )
    subquote_string: list[str] = Field(
        ...,
        description="Include a few more words before and after the value to allow for some context, maximum length 120chars",
    )
    properties: list[Property] = Field(
        ..., description="List of properties of the entity"
    )


class Extraction(BaseModel):
    """Body of the answer, each fact should be a separate object with a body and a list of sources"""

    entities: list[Entity]


def get_response(extraction_target: str, content: str):
    myobject, complete_response = client.chat.completions.create_with_completion(
        messages=[
            {
                "role": "system",
                "content": f"Extract and resolve a list of many {extraction_target} from the following document:",
            },
            {
                "role": "user",
                "content": content,
            },
        ],
        model="gpt-3.5-turbo",
        # model="gpt-4-turbo-preview",
        stream=False,
        max_retries=2,
        temperature=0.3,
        response_model=Extraction,
    )
    return (myobject, complete_response)


def get_response_streaming(extraction_target: str, content: str):
    return client.chat.completions.create_partial(
        messages=[
            {
                "role": "system",
                "content": f"Extract and resolve a list of many {extraction_target} from the following document:",
            },
            {
                "role": "user",
                "content": content,
            },
        ],
        model="gpt-3.5-turbo",
        # model="gpt-4-turbo-preview",
        stream=True,
        max_retries=2,
        temperature=0.3,
        response_model=Extraction,
    )


if __name__ == "__main__":

    ## Data

    content = """
        Source:   https://pycon.lt/2024/schedule

        Dancing with Design
        The talk
        Schedule
        Room: Room 111

        April 4

        09:30–10:30

        Abstract
        Look at your system's design! Are the major structures and technology choices the result of conscious decisions, or have they emerged as the system has evolved? Is the design stuck in a local minima while ever more features are piled into the system? How can we design systems which withstand the major forces acting on a solution?

        We’ll see why system designers should focus deliberately on the constraints and qualities of system design, and avoid getting too distracted by features.

        Prerequisites
        None.

        Description
        In 25 years of programming professionally, most often, and most enjoyably, in Python, I've experienced what makes projects brilliant successes – or epic failures. What will cause your project to succeed – or fail? You’ll help me delve into the demographic characteristics of our industry, dominated by a predominantly young workforce and high turnover. This dynamic has resulted in a lack of experience and inadequate feedback loops, making it challenging to build and maintain firm foundations. Drawing parallels between the software industry and the fashion world, I discuss the pervasive influence of trends and the ephemeral nature of technology adoption, provide a framework for grounding expectations regarding new technologies. We’ll explore the impact of cognitive biases on decision-making within the industry, highlighting biases like the availability cascade, recency effect, and pro-innovation bias. I’ll discuss the challenges faced by software designers, emphasizing that architecture is fundamentally about decision-making and the necessary trade-offs to achieve software qualities. Distinguishing between functionality and software qualities, I emphasize the emergent nature of qualities and the difficulty in capturing and testing these in practice. The discussion challenges the popular wisdom regarding the independence of functionality and qualities, suggesting that adjustments are not always orthogonal. I’ll draw a powerful analogy with the concept of incident forces acting on a system, framing requirements as forces that demand resolution. We explore the resolution of incident forces, factoring them into functionality, qualities, constraints, and principles, helping us direct our attention to where it matters most. The talk concludes with insights into the challenges of navigating the complex space of software qualities, emphasizing the trade-offs and optimization problems inherent in architectural decision-making, finishing with an important message for budding software designers.

        Speakers
        Robert Smallshire
        Robert Smallshire
        Robert has been working with Python for 25 years in the energy and ed-tech sectors, understanding, designing, advocating and implementing effective architectures for sophisticated scientific, enterprise and media production software in Python. He believes in the necessity of a strong engineering culture and enjoys performing the coaching and training necessary to achieve one, while being deliberate with the many and complex trade-offs involved in delivering complex – but not complicated – systems. His most recent venture is with video content production systems, largely implemented in Python.

        Over the last decade, Robert’s Python training courses on Pluralsight have often been in the top-five most popular and have accumulated 1.9 million hours of view time and reached over 1 million paying subscribers. He is co-author of The Python Apprentice, The Python Journeyman, and The Python Master trilogy.

        Affiliation: Sixty North
        Linkedin: https://www.linkedin.com/in/robertsmallshire/


        LLMs: when to use them and when to avoid them
        The talk
        Schedule
        Room: Room 111

        April 4

        16:30–17:30

        Abstract
        At ArjanCodes, we use LLMs in various ways. They are part of the content we produce, we use them in platforms we develop, such as Learntail, they are integrated in automations that streamline our internal processes, and they’re part of our personal workflows, whether that’s for sales and marketing, operations, or software development.

        In this talk, I’ll go over all of these use cases and share the things that we learned from working with LLMs and where LLMs provide us with the most value. Hopefully this wi

        Prerequisites
        Basic Python knowledge

        Description
        Speakers
        Arjan Egges
        Arjan Egges
        I’m a software developer, educator, entrepreneur and content creator with a passion for building beautiful, efficient, and reliable software. I've completed a Master's and PhD in Computer Science and I have more than 20 years of teaching experience. I've launched several startups and designed and built complex software products from scratch. Now, I combine my different experiences in my YouTube videos on the ArjanCodes channel and I offer online courses for developers and companies.

        Affiliation: ArjanCodes
        Linkedin: https://www.linkedin.com/in/arjanegges/
        Website: https://www.arjancodes.com
        Github: https://github.com/ArjanCodes




        Keynote Polars
        The talk
        Schedule
        Room: Room 111

        April 5

        09:30–10:30

        Abstract
        Polars is an OLAP query engine that focusses on the DataFrame use case. Machines have changed a lot in the last decade and Polars is a query engine that is written from scratch in Rust to benefit from the modern hardware.

        Effective parallelism, cache efficient data structures and algorithms are ingrained in its design. This talk will go through recent changes and plans of the project.

        Prerequisites
        Python, data-processing

        Description
        Speakers
        Ritchie Vink
        Ritchie Vink
        Ritchie Vink is the Author of the Polars DataFrame library. Originally he has a background in Civil Engineering, but he soon made the switch to Data/Software development. He has worked as a Machine Learning Engineer and a Software Engineer for 5 years, before he spent all of his time to Polars project. Those years have been filled with side projects to feed his curiosity. In present times he is the CEO of the newly started Polars Inc.

        Github: https://github.com/ritchie46
        Actions
        List of talks
        Keynote Polars | PyCon Lithuania 2024




        The AI Revolution Will Not Be Monopolized: How open-source beats economies of scale, even for LLMs
        The talk
        Schedule
        Room: Room 111

        April 5

        16:30–17:30

        Abstract
        With the latest advancements in Natural Language Processing and Large Language Models (LLMs), and big companies like OpenAI dominating the space, many people wonder: Are we heading further into a black box era with larger and larger models, obscured behind APIs controlled by big tech monopolies? I don’t think so, and in this talk, I’ll show you why.

        Prerequisites
        Interest in data and NLP

        Description
        I’ll dive deeper into the open-source model ecosystem, some common misconceptions about use cases for LLMs in industry, practical real-world examples and how basic principles of software development such as modularity, testability and flexibility still apply. LLMs are a great new tool in our toolkits, but the end goal remains to create a system that does what you want it to do. Explicit is still better than implicit, and composable building blocks still beat huge black boxes.

        As ideas develop, we’re seeing more and more ways to use compute efficiently, producing AI systems that are cheaper to run and easier to control. In this talk, I'll share some practical approaches that you can apply today. If you’re trying to build a system that does a particular thing, you don’t need to transform your request into arbitrary language and call into the largest model that understands arbitrary language the best. The people developing those models are telling that story, but the rest of us aren’t obliged to believe them.

        Speakers
        Ines Montani
        Ines Montani
        Ines Montani is a developer specializing in tools for AI and NLP technology. She’s the co-founder and CEO of Explosion and a core developer of spaCy, a popular open-source library for Natural Language Processing in Python, and Prodigy, a modern annotation tool for creating training data for machine learning models.

        Affiliation: Explosion
        Linkedin: https://www.linkedin.com/in/inesmontani/
        Website: https://explosion.ai
        Github: https://github.com/ines
        Actions
        List of talks
    """

    extraction_target = "Speaker Profiles"
    # extraction_target = "Talk Subjects"
    # extraction_target = "talks & speaker profiles"



    ## Model Properties

    property_object, completion_response = get_response(extraction_target, content)

    print("\n" * 3 + "###property_object" + "\n")
    pprint(property_object)

    print("\n" * 3 + "###property_object.model_json_schema()")
    pprint(property_object.model_json_schema())

    print("\n" * 3 + "###completion_response")
    pprint(completion_response)



    ## Streaming Responses


    # extraction_stream = get_response_streaming(extraction_target, content)

    # console = Console()

    # for extraction in extraction_stream:
    #     obj = extraction.model_dump()
    #     console.clear()
    #     console.print(obj)
