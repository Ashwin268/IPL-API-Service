# 🏏 IPL API Service

A Flask-based API providing IPL data from 2008 to 2024.  

## API Endpoints

### 1. `GET /api/teams`
Returns the list of all IPL teams.

### 2. `GET /api/compareTeams?team1=<team1>&team2=<team2>`
Compare two IPL teams for head-to-head match statistics.

### 3. `GET /api/teamRecords?team=<team>`
Get overall and head-to-head records for a specific team.

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/your-username/ipl-api-service.git
cd ipl-api-service
No, the **response examples** are not strictly required—they’re mainly for clarity so someone using your API knows what to expect.

If you want a shorter, minimal **README**, you can keep just the endpoints, parameters, and instructions to run the API. Here’s a compact version ready to copy:
```

2. Install dependencies:

```bash
pip install flask pandas numpy
```

3. Place the cleaned IPL CSV file in:

```text
content/ipl_matches_cleaned.csv
```

4. Run the API:

```bash
python app.py
```

5. Access endpoints at `http://127.0.0.1:5000/`

## Tech Stack

* Python (Flask)
* Pandas & NumPy
* JSON responses

## Notes

* All data is derived from IPL matches between 2008 and 2024.
