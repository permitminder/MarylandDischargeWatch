"""
State configuration for this MarylandDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "MD"
STATE_NAME = "Maryland"
APP_NAME = "MarylandDischargeWatch"
APP_TAGLINE = "Maryland Discharge Monitoring"
DOMAIN = "marylanddischargewatch.org"
DATA_FILE = "md_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@marylanddischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "EST"
EPA_REGION = 3
