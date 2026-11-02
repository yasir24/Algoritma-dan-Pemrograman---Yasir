# 8.15.2 PRINTING MODELS

import Exercise8_15_1 as printing_functions

unprinted_designs = [
    "model ponsel",
    "model robot",
    "model pesawat"
]

completed_models = []

printing_functions.print_models(
    unprinted_designs,
    completed_models
)

printing_functions.show_completed_models(completed_models)