# Laundry Decider

**Laundry Decider** is a Python-based tool designed to help users compare prices across local laundry stores. The program allows users to manage and compare prices for services like Wash-n-Fold, Wash-n-Press, and Dry Cleaning for various items (e.g., shirts, pants, dresses). The tool uses a CSV file to store laundry store data and allows users to update or add their own local stores for a customized experience.

## Features

- **Customizable CSV File**: Users can create or modify a CSV file to store information about their local laundry stores.
- **Laundry Store Comparisons**: The app compares services such as Wash-n-Fold, Wash-n-Press, and Dry Cleaning across different laundry stores.
- **Price Management**: Handles different price points for services (e.g., price per pound for Wash-n-Fold, item-based pricing for Dry Cleaning).
- **Data Persistence**: The app can update the CSV file with new information before exiting.

## Getting Started

### Prerequisites

To run the program, you will need:

- Python 3.x
- Required Python libraries (if any): You can install them via `pip install -r requirements.txt` (if provided).

### Installation

1. Clone or download the repository to your local machine.
    ```bash
    git clone https://github.com/yourusername/laundry-decider.git
    ```
   
2. Navigate to the project directory:
    ```bash
    cd laundry-decider
    ```

3. (Optional) Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

### Usage

1. Prepare a CSV file with information about local laundry stores. Here is an example of the expected CSV structure:

    | Store Name | Wash-n-Fold - Min Price | Wash-n-Fold - Min Lbs | Wash-n-Fold - Price Per Lb | Wash-n-Press - Shirt | Dry Cleaning - Shirt | Dry Cleaning - Pants | Dry Cleaning - Dress | Dry Cleaning - Suit | Dry Cleaning - Blouse | Dry Cleaning - Coat | Dry Cleaning - Skirt | Dry Cleaning - Sweater | Dry Cleaning - Jacket | Dry Cleaning - Blanket |
    |------------|-------------------------|-----------------------|----------------------------|----------------------|----------------------|-----------------------|-----------------------|----------------------|-----------------------|----------------------|-----------------------|------------------------|------------------------|------------------------|
    | Laundry X  | 10                      | 5                     | 2.5                        | 3                    | 5                    | 7                     | 12                    | 15                   | 7                     | 10                   | 8                     | 6                      | 9                      | 20                     |

2. Run the program:

    ```bash
    python laundry_decider_script.py
    ```

3. Follow the prompts to add or compare laundry store services based on your preferences.

### Customization

- You can edit or create a new CSV file with your local laundry store information to customize the program's functionality for your location.

### Exit Functionality

When you exit the program, it automatically updates the CSV file to match any changes made to the list of laundry stores during the session.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to modify this template according to your specific needs!
