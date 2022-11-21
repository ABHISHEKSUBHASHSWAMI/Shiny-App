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
                box-shadow: rgba(247, 49, 244, 0.8) -20px -20px 100px -20px, rgba(0, 0, 0, 0.7) 0px 30px 60px -30px, rgba(247, 49, 244, 0.6) 0px -2px 6px 0px inset;
                margin-top: 7%;
                margin-left: 12%;
                margin-right: 12%;
                margin-bottom: 7%;
                padding: 70px;
                font-family: 'Poppins', sans-serif;
                background-image: linear-gradient(120deg, #020024 35%, #090979 70%, #0707b5 90%);
                color: #fff;
                width: 75%;
                align-text: center;
            }
            
        """)
    ),
    ui.div(
        ui.h2("SUMMARY EXTRACTOR TOOL")
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
        ui.h4("Steps to use our Summary Extractor Tool"),
        ui.h6("1. Select the type of input you want to give."),
        ui.h6("2. Enter the input in the given field."),
    ),
    ),
    
)

    


def server(input, output, session):
    @output
    @render.ui
    def dyn_ui():
        if input.type() == "Term Search":
            return ui.TagList(
                ui.input_text("x", "Query", placeholder="Search",width='50%'),
                ui.output_text("txt"),
            )

        elif input.type() == "URL":
            return ui.TagList(
                ui.input_text("x", "URL", placeholder="Paste URL",width='50%'),
                ui.output_text("txt"),
            )

        elif input.type() == "Text":
            return ui.TagList(
                ui.input_text_area("x", "Text", placeholder="Paste Text", width='1000px', height='500px'),
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
                return "No Internet Connection..."

        elif input.type() == "URL":
            try:
                text=fetcher.text_fetcher(str(input.x()))
                return 'Summary : \n\n'+summarizer.get_summary(text)
            except Exception as e:
                return "Enter Valid URL"

        elif input.type() == "Text":
            try:
                return 'Summary : \n\n'+summarizer.get_summary(input.x())
            except ValueError:
                warning="Please enter valid text :)"
                return warning
            
app = App(app_ui, server, debug=True)

