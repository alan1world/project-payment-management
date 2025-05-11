# SPDX-FileCopyrightText: 2025-present U.N. Owen <void@some.where>
#
# SPDX-License-Identifier: MIT

from flask import Flask

print(__name__)

app = Flask(__name__)

from project_payment_management import routes

# app.run(debug=False)
app.run(debug=False)


