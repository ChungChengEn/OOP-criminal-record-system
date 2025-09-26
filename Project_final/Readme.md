# Criminal Record Management System

A desktop application for managing and tracking criminal records with efficient search capabilities, built with Python (GUI) and C++ (backend).

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![C++](https://img.shields.io/badge/C++-11-blue.svg)

## 🌟 Features

- **Add Criminal Records**: Create comprehensive criminal profiles with personal information and crime details
- **Advanced Search**: Multiple search options including:
  - Search by criminal name
  - Search by specific time/date
  - Search by time intervals
  - Search by crime type and time combinations
- **Real-time Results**: Instant display of search results with detailed information
- **User-friendly Interface**: Intuitive GUI built with Pygame
- **High Performance**: O(log n) search operations using Red-Black Tree data structures

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- G++ compiler (GCC)
- Make utility

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd criminal-record-system
   ```

2. **Build the C++ backend**
   ```bash
   make
   ```
   Or manually:
   ```bash
   g++ -shared -o mylib.dll -fPIC CrimeRecord.cpp Criminal.cpp Person.cpp System.cpp
   ```

3. **Install Python dependencies**
   ```bash
   pip install pygame cffi
   ```

4. **Run the application**
   ```bash
   python CrimeManager.py
   ```

## 🎮 Usage

### Starting the Application
1. Run `python CrimeManager.py`
2. Press **Space** to start from the loading screen
3. Use the main menu to navigate between functions

### Adding a Criminal Record
1. Click **"New Criminal"** from the main menu
2. Fill in all required fields:
   - Personal information (Name, ID, Gender, Birthday, Location)
   - Crime details (Type, Time, Description)
3. Click **"ADD"** to save the record

### Searching Records
1. Click **"Search"** from the main menu
2. Choose your search method:
   - **Search by Name**: Enter criminal's name
   - **Search by Time**: Enter specific date/time
   - **Search by Time + Crime**: Combine time and crime type filters
   - **Search by Interval**: Search within a time range
3. Results appear instantly in the right panel

### Deleting Records
1. Click **"Delete"** from the main menu
2. Enter the criminal's name and the exact time of the crime record
3. Click **"DELETE"** to remove the record

## 📁 Project Structure

```
criminal-record-system/
├── CrimeManager.py          # Main application entry point
├── addpage.py              # Add new criminal records GUI
├── deletepage.py           # Delete records GUI  
├── searchpage.py           # Search interface GUI
├── object.py               # UI components (Button, InputBox, etc.)
├── function.py             # Utility functions and CFFI integration
├── alert.py                # Alert/notification system
├── System.cpp              # Main C++ system controller
├── CrimeRecord.cpp         # Crime record data structure
├── Criminal.cpp            # Criminal profile management
├── Person.cpp              # Base person class
├── CriminalSystem.h        # Header definitions
├── RBTree_criminalRecord.cpp # Red-Black tree implementation
├── makefile               # Build configuration
└── README.md              # This file
```

## 🏗️ Architecture

The system uses a **hybrid architecture** combining Python and C++:

- **Frontend (Python + Pygame)**: User interface, input validation, event handling
- **Backend (C++)**: Data structures, business logic, search algorithms
- **Integration (CFFI)**: Type-safe communication between Python and C++
- **Data Storage**: Red-Black Trees for O(log n) performance + Hash maps for fast lookups

## 🛠️ Technical Details

### Data Structures
- **5 Red-Black Trees**: One for each crime type (theft, robbery, fraud, murder, others)
- **Hash Map**: For fast criminal name lookups
- **Time Encoding**: Efficient chronological sorting and range queries

### Crime Types Supported
- `Theft` → steal
- `Robbery` → rob  
- `Fraud` → scam
- `Murder` → kill
- `Others` → others

### Performance
- **Search Operations**: O(log n) time complexity
- **Insert/Delete**: O(log n) time complexity  
- **Memory Efficient**: Balanced tree structures prevent degradation

## 🎯 Controls

| Key/Action | Function |
|------------|----------|
| `Space` | Start application from loading screen |
| `Escape` | Close current page/return to menu |
| `Enter` | Submit current form |
| `Mouse Click` | Navigate UI elements |
| `Backspace` | Delete characters in input fields |

## 🔧 Configuration

### Building for Different Platforms

**Windows:**
```bash
g++ -shared -o mylib.dll -fPIC CrimeRecord.cpp Criminal.cpp Person.cpp System.cpp
```

**Linux:**
```bash
g++ -shared -o mylib.so -fPIC CrimeRecord.cpp Criminal.cpp Person.cpp System.cpp
```

**macOS:**
```bash
g++ -shared -o mylib.dylib -fPIC CrimeRecord.cpp Criminal.cpp Person.cpp System.cpp
```

Update the library name in `function.py` accordingly.

## 🐛 Troubleshooting

### Common Issues

**"mylib.dll not found" error:**
- Make sure you ran `make` or compiled the C++ files manually
- Check that the .dll file exists in the project directory

**GUI not displaying correctly:**
- Ensure Pygame is properly installed: `pip install pygame`
- Check that all image and font files are in the correct directories

**Search returns no results:**
- Verify the exact format for time inputs (numbers only)
- Criminal names are case-sensitive
- Make sure records exist in the system

**Build errors:**
- Ensure G++ compiler is installed and in PATH
- Check that all .cpp and .h files are present
- Try cleaning and rebuilding: `make clean && make`
