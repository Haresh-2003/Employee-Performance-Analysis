# Employee Performance and Productivity Analysis

## Project Overview
This project analyzes employee performance and productivity data to understand key factors influencing efficiency in the workplace. It includes data cleaning, exploratory data analysis (EDA), correlation analysis, statistical testing, and visualizations to derive actionable insights.

This project is developed as part of an internship at SVCode Tech Company.

## Features
- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Correlation Analysis
- Statistical Testing (T-test)
- Data Visualization using Matplotlib and Seaborn
- Insights on Training Program Effectiveness

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy (Statistical Analysis)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/employee-performance-analysis.git
   cd employee-performance-analysis
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place the dataset (`Extended_Employee_Performance_and_Productivity_Data.csv`) in the `data/` directory.
2. Run the main analysis script:
   ```bash
   python performance_analysis.py
   ```
3. View the generated reports and visualizations in the `output/` directory.

## Data Sources
The dataset includes columns such as:
- `EmployeeID`: Unique identifier for each employee.
- `Age`: Age of the employee.
- `Department`: The department they belong to.
- `Experience`: Years of experience.
- `Training_Program`: Whether the employee attended training (attended/not_attended).
- `Productivity_Score`: A numerical score indicating productivity level.

## Expected Outputs
- Correlation analysis between employee attributes and productivity.
- Identification of factors affecting employee performance.
- Statistical comparison of training effectiveness (T-test results).
- Data visualizations such as heatmaps, box plots, and pair plots.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature/fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

## Contact
For any inquiries, please contact [HARESH] at [hareshp.s1066@gmail.com].
