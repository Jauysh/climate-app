# Climate Data Dashboard 🌍

A Streamlit web application for visualizing and analyzing climate data trends including temperature changes, CO₂ levels, and sea level rise.

## Features

- **Interactive Dashboard**: Multi-page navigation with different climate metrics
- **Temperature Trends**: Global temperature analysis with statistical insights
- **CO₂ Levels**: Atmospheric carbon dioxide concentration tracking
- **Sea Level Rise**: Global sea level change monitoring
- **Data Visualization**: Interactive charts using Plotly
- **Responsive Design**: Clean, mobile-friendly interface

## Pages

1. **Overview**: Key climate metrics and recent trends
2. **Temperature Trends**: Detailed temperature analysis and statistics
3. **CO₂ Levels**: Atmospheric CO₂ concentration and correlation with temperature
4. **Sea Level Rise**: Sea level changes and rise rates

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Jauysh/climate-app.git
cd climate-app
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Requirements

- Python 3.9+
- Streamlit 1.28.0
- Pandas 2.1.0
- Plotly 5.15.0
- NumPy 1.24.0

## Project Structure

```
climate-app/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .github/
    └── workflows/
        └── deploy.yml    # GitHub Actions workflow for deployment
```

## Data Sources

This application currently uses simulated climate data that demonstrates realistic trends:
- Temperature: Simulated global warming trend (2°C increase over 25 years)
- CO₂ Levels: Simulated atmospheric concentration increase (100 ppm over 25 years)
- Sea Level: Simulated sea level rise (100mm over 25 years)

*Note: For production use, integrate with real climate data APIs like NASA's Global Climate Change API or NOAA's climate data services.*

## Deployment

### Streamlit Cloud (Recommended)
1. Fork this repository
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Connect your GitHub account
4. Select this repository and set the main file to `app.py`
5. Deploy!

### Local Deployment
```bash
streamlit run app.py
```

The app will be available at `http://localhost:8501`

## GitHub Actions

This repository includes a GitHub Actions workflow that:
- Runs tests on multiple Python versions
- Checks code quality with flake8
- Validates dependencies
- Provides deployment instructions

## Contributing

1. Fork the project
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Data visualization with [Plotly](https://plotly.com/)
- Icons and emojis for better user experience

---

**🌱 Climate awareness starts with understanding the data.**
