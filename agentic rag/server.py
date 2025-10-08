from crewai import Crew, Agent , Task , LLM
import litserve as ls
from crewai_tools import FirecrawlCrawlWebsiteTool , QdrantVectorSearchTool

class AgenticRAGAPI(ls.LitAPI):
    def setup(self, device):
        llm = LLM(model="ollama/qwen3:4b")

        researcher_agent = Agent(
            role="Senior Researcher",
            goal= "Conduct in-depth research on a given topic and provide comprehensive insights.",
            backstory="An experienced researcher skilled in gathering and analyzing information from various sources.",
            tools=[FirecrawlCrawlWebsiteTool(), VectorDBSearchTool() ],
            llm=llm
        )

        researcher_task = Task(
            description="research about {query}",
            agent=researcher_agent
        )

        writer_agent = Agent(
            role="Senior Writer",
            goal="use the insights to answer user query and create well-structured and engaging content based on the research findings.",
            backstory="A creative writer with expertise in transforming research data into compelling narratives.",
        )
        writer_task = Task(
            description="write a detailed article on {query} using the research findings.",
            agent=writer_agent
        )
        self.crew = Crew(
            agents=[researcher_agent, writer_agent],
            tasks=[researcher_task, writer_task]
        )

    def decode_request(self, request):
        return request['query']
    
    def predict(self, query):
        return self.crew.kickoff(inputs={"query": query})
    
    def encode_response(self, output):
        return {"output": output}
    
if __name__ == "__main__":
    api = AgenticRAGAPI()
    server = ls.LitServer(api)
    server.run(port=8000)