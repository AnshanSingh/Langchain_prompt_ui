from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Summarize the research paper "{paper_input}" in a {style_input} style.
The summary should be {length_input} in length.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True # for ensure we pass all the placeholder so he trigger the error
)

template.save('template.json') # to save the template in json format in new file










# The Summary = Basically we work on this file how to use resuable prompt 
# like we can load prompt template in multiple page with the use of load_prompt 
# so that can make reusable