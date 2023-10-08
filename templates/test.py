# Assuming forecast_vol contains the forecasted sales values
forecast_vol = [100, 150, 200, 180, 220, 250, 210]  # Replace with your actual values

# Create the HTML template
html_template = """
<section id="textbody">
    <div class="content">
        <header>
            <h1>Sales Forecast for the next 7 days</h1>
        </header>
        <p>Sales Forecast: <b>{}</b></p>
    </div>
</section>
"""

# Insert the forecast_vol into the template
html_output = html_template.format(forecast_vol)

# Print or use the HTML output
print(html_output)
