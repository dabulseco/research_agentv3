Additional Setup (if needed):
If you still encounter issues, create a .env file in your project directory with:

bash# .env file
OLLAMA_BASE_URL=http://localhost:11434
OPENAI_API_KEY=not-needed

Or set environment variable before running:

Windows (Command Prompt):
cmdset OPENAI_API_KEY=not-needed
streamlit run app.py

Windows (PowerShell):
powershell$env:OPENAI_API_KEY="not-needed"
streamlit run app.py


Linux/Mac:
bashexport OPENAI_API_KEY=not-needed
streamlit run app.py


Verify Ollama is Running:
Make sure Ollama is running locally:
bashollama serve
Then in another terminal, test it:
bashollama list
The app should now work completely offline with your local Ollama models! Let me know if you encounter any other issues.


Prompt:

Prompt 1:
I want to research use of AI in education. First, I want to focus on published papers that has data-driven recommendations on AI use in education based on research. Second, provide other guidance for use of AI in education based on best practices even if research data does not exist and third, provide any recommendations by experts in AI in education as approaches to take.  I want to emphasize Human-Computer interactions especially involving teachers and how best to guide them and will always focus on Human-in-the-Loop interactions between AI and educators and students for any AI applied in education. My goal is to create a comprehensive guide to faculty at community colleges that are building programs that implement AI in education

Prompt 1:
I want to write a blog post that introduces the value of AI Tutors based on Retrieval Augmented Generation (RAG) to student learning.  I want to first base the blog on any published literature on the topic, second based on recommendations by educators and experts, and third based on any recommended advice provided by others. The goal is to use this to introduce data that we have generated on RAG accuracy which depends on algorithms used to create and then embed and retrieve content. Specifically, we evaluate the importance of embedding models, re-ranking of retrieval results, the use of various vector databases including those that are purely semantic vs. others that are hybrid storage and retrieval, like Milvus, that allows both semantic and lexical storage and retrieval. The goal is to provide information that shows how important this technology can be in contributing to AI in Education, and how important the algorithms used to implement them are. We continue this topic by showing how transcript analysis using Bloom's taxonomy framework can be used to gain insights into student's educational journey through their interaction with AI Tutors built with this technology.  I want the blog entry to be comprehensive but accurate with references and citations if possible.

Prompt 3:
Compose a comprehensive research report analyzing the future of higher education in the age of pervasive Artificial Intelligence (AI). Your report should address the following, with a focus on actionable recommendations for institutions now:

1. Historical Context & Current Infrastructure (Approximately 25% of Report):

    Brief History: Trace the evolution of higher education in the Western model (focusing on the US/Europe initially, but acknowledging global variations are welcome), from its origins in medieval universities to the modern, largely standardized system. Highlight key historical shifts (e.g., the Morrill Act, the rise of research universities, the community college movement).
    Current Infrastructure: Detail the current operational infrastructure of higher education institutions. This should include (but is not limited to): faculty roles & tenure systems, curriculum development processes, assessment methods, administrative structures, funding models (public vs. private, tuition dependence), and the physical campus model.
    Historical Conflict: Critically analyze how the historical development and current infrastructure of higher education inherently create conflict with the potential for widespread AI integration. Specifically, address how traditional structures (e.g., faculty workload models, standardized curricula, assessment practices) impede or contradict AI's capabilities and potential benefits. Consider issues like intellectual property, academic integrity, and the role of human interaction.

2. AI Integration Across Educational Phases (Approximately 50% of Report):

    Admissions & Recruitment: How can AI be used ethically and effectively in admissions, financial aid, and student recruitment? Address potential biases and equity concerns.
    Curriculum Design & Delivery: Explore AI's role in personalized learning, adaptive assessments, automated content creation, and virtual/augmented reality learning environments. Discuss the impact on course design and the potential for AI-driven curriculum updates.
    Teaching & Assessment: Analyze how AI can assist instructors (e.g., grading, feedback, identifying at-risk students) while maintaining academic integrity. Examine the future of assessment in an AI-assisted environment – what skills and knowledge become more important to assess?
    Research & Scholarship: Discuss AI's role in accelerating research, analyzing data, and facilitating collaboration. Address ethical considerations related to AI-generated research and authorship.
    Student Support & Services: How can AI-powered chatbots, virtual advisors, and personalized support systems improve student outcomes and retention?

3. Future Vision & Recommendations (Approximately 25% of Report):

    Future Scenarios: Present 2-3 plausible future scenarios for higher education incorporating AI, ranging from optimistic to cautionary.
    Actionable Recommendations: Provide concrete, actionable recommendations for higher education institutions, policymakers, and faculty now to proactively adapt to the AI-driven future. These should address systemic changes needed, potential pilot programs, and strategies for faculty training and development. Consider the ethical implications of each recommendation.
    Challenges & Risks: Outline the major challenges and risks associated with AI integration in higher education (e.g., job displacement, digital divide, over-reliance on technology, erosion of critical thinking).

Evaluation Criteria:

    Depth of Research: Demonstrates a thorough understanding of the history, current state, and future trends of higher education and AI. Citations are required.
    Critical Analysis: Provides a nuanced and critical assessment of the conflicts between traditional structures and AI integration.
    Actionability: Recommendations are specific, practical, and address the challenges realistically.
    Ethical Considerations: Explicitly addresses the ethical implications of AI in education.
    Clarity & Organization: Report is well-written, logically organized, and easy to understand.
    Forward-Thinking: Demonstrates an ability to anticipate future challenges and opportunities."

#end Prompt 3

Prompt 4:
I want to know all of the different algorithms used to create RAG-based AI Tutors.  I want to see what is published with data presented showing efficacy and a comparison of the efficacy of the RAG that is dependent on the algorithms used to develop it. Cover all aspects of building RAG including embedding model, vector database and retrieval methods, if other interventions like re-ranking was used and what LLMs were used with the RAG.  If they used it to test student use as part of the efficacy please include this data.  I want a blog written that is a comprehensive review of the literature and can present the kinds of applications RAG can be used for with measured student outcomes when they exist.

Prompt 5:
I want to build a software platform that will take two or more DNA sequences input as FASTA files, and assign each nucleotide to a musical note based on an open source embedding model that does this, the plays the pairs (or more) notes together at different octaves (so we can distinguish them).  My goal is to use this approach to identify mutations in DNA sequences or errors/differences in DNA sequences using sound and not vision, staying within the field of data sonification.  I want to then use this same approach to demonstrate the analysis of mutations that occur in cancer so will need some specific examples saved as FASTA files that I can use in this demo.  Use python as the main coding language with a UI based on streamlit.  If any LLM is needed I want that to be based on local LLMs as installed using Ollama and only want the internet to be used to search for DNA sequences (preferably at NCBI) or to do web searches for more content and context using a headless browser like Selenium.  If this is best handled using an agent, I want the code to be based on crew.ai for the agentic framework and workflow.  The output of this will be sequence alignment (or multiple sequence alignment) plots and auditory output as each nucleotide sequence is highlighted and played over the computer speaker.
