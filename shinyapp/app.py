from shiny import App, render, ui
import fetcher
import summarizer


app_ui = ui.page_fluid(
    ui.tags.head(
        ui.tags.style("""
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
            body {
                box-sizing: border-box;
                border-radius: 35px;
                margin-top: 7%;
                margin-left: 12%;
                margin-right: 12%;
                margin-bottom: 7%;
                padding: 70px;
                font-family: 'Poppins', sans-serif;
                background-color: #10002E;
                color: #fff;
                width: 75%;
                border: 3px solid white;
                align-text: center;
            }
            
        """)
    ),
    ui.div(
        ui.h2("SUMMARY EXTRACTOR")
    ),
    ui.div(
        ui.input_radio_buttons(
        "type",
        ui.h6("Select the type of input"),
        choices=["Term Search","URL","Text"],
    ),
    ui.div(
        ui.output_ui("dyn_ui"),
    ),
    ui.div(
        {"style":"align-text:center;font-family:'Gill Sans', sans-serif;margin-top:15%"},
        ui.h4("How to use our Summary Extractor :"),
        ui.h6("1. Select the type of input you want to give."),
        ui.h6("2. Enter the input in the given field."),
    ),
    ui.div(
        {"style":"align-text:center;font-family:'Gill Sans', sans-serif;margin-top:7%"},
        ui.h4("What is Text Summarizer ?"),
        ui.p("A Text Summarizer is an online tool that wraps up a text to a specified short length. It condenses a long article to main points. The need for text summarizers is increasing day by day, because of time constraints. People are looking for shortcut methods to learn ideas in lesser time. Even text summarizers are helping them to decide whether a book, a research paper, or an article is worth reading or not."),
        ui.h4("Approaches in auto summarization:"),
        ui.h5("Extractive Summarization: "),
        ui.p("This approach entails the method to extract keywords and phrases from sentences and then joining them to produce a compact meaningful summary."),
        ui.h5("Abstractive Summarization :"),
        ui.p("In this summary generator, algorithms are developed in such a way to reproduce a long text into a shorter one by NLP. It retains its meaning but changes the structure of sentences."),
    ),

    ui.div(
        {"style":"align-text:center;font-family:'Gill Sans', sans-serif;margin-top:7%"},
        ui.h4("How Does Text Summerization Work?"),
        ui.p('''Trained by machine learning, paraphraser.io text summarizer uses the concept of abstractive summarization to summarize a book, an article, or a research paper. This summarize tool uses NLP to create novel sentences and generates a summary in which the main idea remains intact. It is an advanced-level tool that uses AI for its work. Therefore, the summary produced by this tool appears to be flawless and inflow.'''),
        
    ),
    ui.div(
        {"style":"align-text:center;font-family:'Gill Sans', sans-serif;margin-top:7%"},
        ui.h4("Users of Text Summarization Tool"),
        ui.h5("Students :"),
        ui.p("A text summarizer helps students to condense difficult concepts by summarizing them. They get the know-how of complex articles and books. Moreover, manual summarizing can be very time-consuming. They use a text summarizer to solve their assignments in lesser time."),
        ui.h5("Researchers :"),
        ui.p("Researchers use text summarizers to condense their research papers. They can use the summary to explain their research to others. It is a time-saving tool for them."),
        ui.h5("Businessmen :"),
        ui.p("Businessmen use text summarizers to condense their business reports. They can use the summary to explain their business to others. It is a time-saving tool for them."),
        ui.h5("Bloggers :"),
        ui.p("Bloggers use text summarizers to condense their blog posts. They can use the summary to explain their blog to others. It is a time-saving tool for them."),
        ui.h5("Journalists :"),
        ui.p("Journalists use text summarizers to condense their news articles. They can use the summary to explain their news to others. It is a time-saving tool for them."),
        ui.h5("Content Writers :"),
        ui.p("Content writers use text summarizers to condense their content. They can use the summary to explain their content to others. It is a time-saving tool for them."),
        ui.h5("Teachers :"),
        ui.p("Teachers use text summarizers to condense their lessons. They can use the summary to explain their lessons to others. It is a time-saving tool for them."),
        ui.h5("Learners :"),
        ui.p("Learners use text summarizers to condense their lessons. They can use the summary to explain their lessons to others. It is a time-saving tool for them."),
    ),
    ui.div(
        {"style":"font-family:'Gill Sans', sans-serif;margin-top:7%;"},
        ui.h6("Made with ❤️"),
    )
    ),
    
)

    


def server(input, output, session):
    @output
    @render.ui
    def dyn_ui():
        if input.type() == "Term Search":
            return ui.TagList(
                ui.input_text("x", "Query", placeholder="Search",width='700px'),
                ui.output_text("txt"),
            )

        elif input.type() == "URL":
            return ui.TagList(
                ui.input_text("x", "URL", placeholder="Paste URL",width='700px'),
                ui.output_text("txt"),
            )

        elif input.type() == "Text":
            return ui.TagList(
                ui.input_text_area("x", "Text", placeholder="Paste Text", width='1200px', height='500px'),
                ui.output_text("txt"),
        )

    @output
    @render.text
    def txt():
        if input.type() == "Term Search":
            try:
                url=fetcher.query_to_url(input.x())
                text=fetcher.wiki_fetcher(url)
                return "Summary : \n\n"+summarizer.get_summary(text)
            except Exception as e:
                return e

        elif input.type() == "URL":
            try:
                text=fetcher.text_fetcher(str(input.x()))
                return 'Summary : \n\n'+summarizer.get_summary(text)
            except Exception as e:
                return "Enter valid URL :)"

        elif input.type() == "Text":
            try:
                return 'Summary : \n\n'+summarizer.get_summary(input.x())
            except ValueError:
                warning="Please enter valid text :)"
                return warning
            
app = App(app_ui, server, debug=True)
