# Criminal Record System - Design Document

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Module Design](#module-design)
4. [Data Structure Design](#data-structure-design)
5. [User Interface Design](#user-interface-design)
6. [Security Considerations](#security-considerations)
7. [Design Patterns & Principles](#design-patterns--principles)
8. [Future Improvements](#future-improvements)

---

## 1. Project Overview

### 1.1 Purpose
The Criminal Record System is a desktop application designed to manage and track criminal records efficiently. It provides functionality for storing, searching, and managing criminal information along with their associated crime records.

### 1.2 Scope
- **Add Criminal Records**: Create new criminal profiles with personal information and crime details
- **Delete Records**: Remove specific crime records based on criminal name and time
- **Search Operations**: Multiple search capabilities including:
  - Search by specific time
  - Search by time intervals
  - Search by crime type and time
  - Search by criminal name
- **Data Visualization**: Display search results in an organized, user-friendly interface

### 1.3 Main Objectives
- Provide efficient storage and retrieval of criminal records using Red-Black Trees
- Offer an intuitive graphical user interface built with Pygame
- Ensure fast search operations with O(log n) complexity
- Support multiple search criteria for comprehensive data analysis
- Maintain data integrity and system reliability

### 1.4 Technology Stack
- **Backend**: C++ with Red-Black Tree implementation
- **Frontend**: Python with Pygame framework
- **Integration**: CFFI (C Foreign Function Interface)
- **Build System**: GNU Make with g++ compiler

---

## 2. System Architecture

### 2.1 High-Level Architecture

The system follows a **layered architecture** with clear separation between presentation, business logic, and data layers:

```
┌─────────────────────────────────────────┐
│           Presentation Layer            │
│        (Python + Pygame GUI)           │
├─────────────────────────────────────────┤
│          Integration Layer              │
│              (CFFI)                     │
├─────────────────────────────────────────┤
│         Business Logic Layer           │
│         (C++ System Class)             │
├─────────────────────────────────────────┤
│           Data Layer                   │
│    (Red-Black Trees + Hash Maps)      │
└─────────────────────────────────────────┘
```

### 2.2 Component Interaction Diagram

```
Python GUI ←→ CFFI Interface ←→ C++ System Class
                                      ↓
                              ┌───────────────┐
                              │  Data Storage │
                              ├───────────────┤
                              │ • 5 RB-Trees  │
                              │   (by crime)  │
                              │ • Hash Map    │
                              │   (criminals) │
                              └───────────────┘
```

### 2.3 Core Components

| Component | Technology | Responsibility |
|-----------|------------|----------------|
| **GUI Layer** | Python/Pygame | User interaction, input validation, result display |
| **System Controller** | C++ | Business logic, data operations coordination |
| **Data Structures** | C++ | Efficient storage and retrieval using RB-Trees |
| **Integration Layer** | CFFI | Cross-language communication |

---

## 3. Module Design

### 3.1 Python Modules

#### 3.1.1 CrimeManager.py (Main Controller)
**Responsibility**: Main application controller and event handling
- Manages application lifecycle
- Coordinates between different pages
- Handles global event processing

**Key Functions**:
- `Loading_Page()`: Initial loading screen
- `Crime_Manager()`: Main menu interface
- `Add_Criminal_Page()`: Add new criminal records
- `Delete_Page()`: Delete existing records
- `Search_Page()`: Search interface

#### 3.1.2 AddPage Class
**Responsibility**: New criminal record creation interface
- Input validation for all required fields
- Crime type selection via dropdown menu
- Data formatting before backend submission

**Key Attributes**:
```python
- selectionType = ["Theft", "Robbery", "Fraud", "Murder", "others..."]
- Input fields: name, ID, gender, birthday, location, description
- Time fields: year, month, day, hour, minute
```

#### 3.1.3 SearchPage Class
**Responsibility**: Search interface with multiple search options
- Time-based searches
- Name-based searches  
- Crime type filtering
- Results display coordination

#### 3.1.4 Object Classes

| Class | Purpose |
|-------|---------|
| `Button` | Interactive UI buttons with hover effects |
| `InputBox` | Text input fields with validation |
| `Table` | Data display container |
| `Block` | Individual record display unit |
| `Alert` | System notifications and warnings |

### 3.2 C++ Modules

#### 3.2.1 System Class
**Responsibility**: Core business logic and data management
```cpp
class System {
private:
    RB_Tree crimeTree[5];           // Trees for each crime type
    map<string, int> treeNumber;     // Crime type to tree mapping
    map<string, Criminal*> criminal; // Criminal name to object mapping

public:
    void insert(params...);          // Add new crime record
    void erase(params...);           // Delete crime record
    int searchByTime(params...);     // Time-based search
    int searchByName(params...);     // Name-based search
    // Additional search methods...
};
```

#### 3.2.2 Criminal Class (Inherits from Person)
**Responsibility**: Individual criminal data management
```cpp
class Criminal : public Person {
private:
    int numOfRecord;
    vector<CrimeRecord*> records;

public:
    void addcrimeRecord(CrimeRecord* record);
    void deletecrimeRecord(CrimeRecord* record);
    void outputAllRecord(char** array, int row, int col);
    CrimeRecord* getRecord_time(vector<int> t);
};
```

#### 3.2.3 CrimeRecord Class
**Responsibility**: Individual crime record data structure
```cpp
class CrimeRecord {
private:
    string type, description;
    int time;                       // Encoded time for sorting
    string time_str;                // Human-readable time
    CrimeRecord *left, *right, *p;  // Tree navigation
    int color;                      // Red-Black tree coloring
    Criminal *criminal;             // Back reference

public:
    // Time encoding/decoding methods
    // Tree manipulation methods
    // Data access methods
};
```

#### 3.2.4 Red-Black Tree Implementation
**Responsibility**: Efficient data storage and retrieval
- **Time Complexity**: O(log n) for insert, delete, search
- **Features**: 
  - Self-balancing binary search tree
  - Time-based indexing
  - Range query support

**Key Operations**:
```cpp
void Insert(RB_Tree& T, Node* z);
void Delete(RB_Tree& T, Node* z);
vector<Node*> SearchTime(int year, int month, int day, int hour, int minute);
vector<Node*> SearchInterval(time1, time2);
```

---

## 4. Data Structure Design

### 4.1 Data Storage Strategy

The system uses a **hybrid approach** combining multiple data structures for optimal performance:

#### 4.1.1 Red-Black Trees (5 trees)
```
Tree Index | Crime Type | Purpose
-----------|------------|----------
    0      |   steal    | Theft records
    1      |   rob      | Robbery records  
    2      |   scam     | Fraud records
    3      |   kill     | Murder records
    4      |   others   | Other crime types
```

**Advantages**:
- O(log n) search, insert, delete operations
- Automatic balancing maintains performance
- Efficient range queries for time intervals
- Memory-efficient compared to hash tables for sorted data

#### 4.1.2 Hash Map (Criminal Index)
```cpp
map<string, Criminal*> criminal;  // Criminal name → Criminal object
```

**Purpose**: Fast O(1) criminal lookup by name

#### 4.1.3 Time Encoding Algorithm
```cpp
// Convert date/time to integer for tree sorting
time = year * 525600 + (cumulative_days + day) * 1440 + hour * 60 + minute;
```

**Benefits**:
- Enables chronological ordering
- Supports efficient range queries
- Compact integer representation

### 4.2 Data Flow Diagram

```
User Input → GUI Validation → CFFI Interface → C++ System
                                                    ↓
Criminal Map ← Update ← Business Logic → RB-Tree Operations
    ↓                                           ↓
Search Results ← Format ← Data Retrieval ← Tree Search
    ↓
GUI Display ← CFFI Response ← Result Array
```

### 4.3 Memory Management

| Component | Memory Strategy |
|-----------|----------------|
| **C++ Objects** | Manual memory management with new/delete |
| **Python Objects** | Automatic garbage collection |
| **CFFI Buffers** | Managed by CFFI with explicit cleanup |
| **Result Arrays** | Pre-allocated fixed-size char arrays |

---

## 5. User Interface Design

### 5.1 Interface Architecture

The GUI follows a **state-based design** with multiple screens:

```
Loading Screen → Main Menu → [Add Page / Delete Page / Search Page]
                    ↑                           ↓
                    └─── Return to Menu ────────┘
```

### 5.2 Screen Specifications

#### 5.2.1 Main Menu (Crime_Manager)
- **Layout**: Left sidebar with buttons, right panel for results
- **Components**: Add, Delete, Search buttons
- **Background**: Professional crime management theme

#### 5.2.2 Add Criminal Page
- **Form Fields**: 
  - Personal Info: Name, ID, Gender, Birthday, Location
  - Crime Info: Type (dropdown), Time (5 fields), Description
- **Validation**: Real-time input validation with alerts
- **Dimensions**: 1000x600 pixels, centered modal

#### 5.2.3 Search Page
- **Search Options**: 
  - By Name
  - By Time (exact)
  - By Time Range
  - By Crime Type + Time combinations
- **Results**: Dynamic block-based display

### 5.3 UI Component Standards

| Component | Specifications |
|-----------|----------------|
| **Buttons** | Blue theme (#5069B5), hover effects, consistent sizing |
| **Input Boxes** | White background, gray placeholder text, focus highlighting |
| **Color Scheme** | Professional blue/gray palette |
| **Typography** | Calibri font family, consistent sizing |
| **Responsiveness** | Window resizing support |

---

## 6. Security Considerations

### 6.1 Current Security Measures

#### 6.1.1 Input Validation
- **Client-Side**: Python GUI validates input format and requirements
- **Data Type Checking**: Ensures numeric inputs for time fields
- **Required Field Validation**: Prevents incomplete record submission

#### 6.1.2 Memory Safety
- **CFFI Integration**: Type-safe C/Python interface
- **Buffer Management**: Fixed-size arrays prevent overflow
- **Error Handling**: Graceful handling of invalid operations

### 6.2 Security Limitations

⚠️ **Current Weaknesses**:
- No user authentication or authorization
- No data encryption at rest or in transit
- No audit logging of operations
- Direct file system access without permissions
- No input sanitization for SQL injection (though not using SQL)

### 6.3 Data Integrity

| Measure | Implementation |
|---------|----------------|
| **Referential Integrity** | Criminal-CrimeRecord relationships maintained |
| **Data Validation** | Type checking and format validation |
| **Memory Management** | Proper cleanup prevents memory leaks |
| **Error Recovery** | Graceful handling of invalid operations |

---

## 7. Design Patterns & Principles

### 7.1 Architectural Patterns

#### 7.1.1 Layered Architecture
The system implements a clear **3-tier architecture**:
- **Presentation Layer**: Pygame GUI
- **Business Layer**: C++ System class
- **Data Layer**: Red-Black Trees + Hash Maps

#### 7.1.2 Model-View-Controller (MVC)
- **Model**: C++ data structures (Criminal, CrimeRecord)
- **View**: Python GUI classes (AddPage, SearchPage, etc.)
- **Controller**: CrimeManager.py + System.cpp coordination

### 7.2 Design Patterns

#### 7.2.1 Facade Pattern
```cpp
// System class provides simplified interface to complex subsystems
class System {
    // Hides complexity of multiple RB-Trees and hash maps
    // Provides simple methods like searchByName(), insert(), etc.
};
```

#### 7.2.2 Strategy Pattern
```python
# Different search strategies based on user selection
def Search_Page():
    if search_by_name_clicked:
        searchbyName()
    elif search_by_time_clicked:
        searchbyTime()
    # etc.
```

#### 7.2.3 Factory Pattern (Implicit)
```cpp
// CrimeRecord creation based on crime type
CrimeRecord* record = new CrimeRecord(type, description, ...);
// Inserted into appropriate tree based on type
```

### 7.3 SOLID Principles Application

| Principle | Implementation |
|-----------|----------------|
| **Single Responsibility** | Each class has one clear purpose (Criminal, CrimeRecord, System) |
| **Open/Closed** | New crime types can be added without modifying existing code |
| **Liskov Substitution** | Criminal properly extends Person |
| **Interface Segregation** | CFFI interface only exposes necessary methods |
| **Dependency Inversion** | GUI depends on abstractions, not concrete C++ implementations |

### 7.4 Language Integration Pattern

```
Python (High-level GUI) ←→ CFFI Bridge ←→ C++ (Performance-critical operations)
```

**Benefits**:
- Combines Python's ease of development with C++'s performance
- Clear separation of concerns
- Type-safe inter-language communication

---

## 8. Future Improvements

### 8.1 Security Enhancements

#### 8.1.1 Authentication System
- **User Management**: Role-based access control (Admin, Officer, Viewer)
- **Login System**: Secure authentication with password hashing
- **Session Management**: Token-based session handling
- **Audit Trail**: Log all operations with user attribution

#### 8.1.2 Data Protection
- **Encryption**: AES encryption for sensitive data at rest
- **Network Security**: TLS for any future network communications
- **Input Sanitization**: Enhanced validation to prevent injection attacks
- **Data Backup**: Automated backup with encryption

### 8.2 Scalability Improvements

#### 8.2.1 Database Integration
```sql
-- Replace in-memory storage with persistent database
CREATE TABLE criminals (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    gender VARCHAR(20),
    birthday DATE,
    location VARCHAR(200)
);

CREATE TABLE crime_records (
    record_id SERIAL PRIMARY KEY,
    criminal_id VARCHAR(50) REFERENCES criminals(id),
    crime_type VARCHAR(50),
    crime_time TIMESTAMP,
    description TEXT,
    location VARCHAR(200)
);

-- Indexes for performance
CREATE INDEX idx_crime_time ON crime_records(crime_time);
CREATE INDEX idx_crime_type ON crime_records(crime_type);
CREATE INDEX idx_criminal_name ON criminals(name);
```

#### 8.2.2 Distributed Architecture
- **Microservices**: Break into smaller, independent services
- **API Gateway**: RESTful API for external integrations
- **Load Balancing**: Handle multiple concurrent users
- **Caching**: Redis/Memcached for frequently accessed data

### 8.3 Feature Enhancements

#### 8.3.1 Advanced Search
- **Fuzzy Search**: Approximate string matching for names
- **Geographic Search**: Location-based crime analysis
- **Pattern Recognition**: Machine learning for crime pattern detection
- **Advanced Filters**: Multiple criteria combination with AND/OR logic

#### 8.3.2 Reporting & Analytics
- **Statistical Reports**: Crime trends and statistics
- **Data Visualization**: Charts and graphs using libraries like Matplotlib
- **Export Functionality**: PDF, CSV, Excel report generation
- **Dashboard**: Real-time crime statistics overview

### 8.4 User Experience Improvements

#### 8.4.1 Modern UI Framework
- **Migration to Qt/Tkinter**: More professional appearance
- **Responsive Design**: Better handling of different screen sizes
- **Dark/Light Themes**: User preference support
- **Internationalization**: Multi-language support

#### 8.4.2 Performance Optimizations
```cpp
// Potential improvements
class System {
    // Add caching for frequent queries
    unordered_map<string, vector<CrimeRecord*>> searchCache;
    
    // Parallel processing for large datasets
    void parallelSearch(/* parameters */);
    
    // Memory pooling for better allocation
    ObjectPool<CrimeRecord> recordPool;
};
```

### 8.5 Integration Capabilities

#### 8.5.1 External System Integration
- **Law Enforcement APIs**: Integration with national crime databases
- **Court Systems**: Case management integration
- **Background Check Services**: Automated verification
- **Notification Systems**: SMS/Email alerts for new records

#### 8.5.2 Data Import/Export
- **File Formats**: Support for CSV, JSON, XML
- **Batch Operations**: Bulk import/export functionality
- **Data Migration**: Tools for transitioning from legacy systems
- **Synchronization**: Real-time sync with external databases

### 8.6 Monitoring & Maintenance

#### 8.6.1 System Monitoring
- **Performance Metrics**: Response time tracking
- **Error Logging**: Comprehensive error tracking and reporting
- **Health Checks**: System status monitoring
- **Usage Analytics**: User behavior and system utilization tracking

#### 8.6.2 Maintenance Tools
- **Automated Testing**: Unit and integration test suites
- **Deployment Pipeline**: CI/CD for reliable updates
- **Configuration Management**: Environment-specific configurations
- **Documentation**: Auto-generated API documentation

---

## Conclusion

The Criminal Record System demonstrates a well-structured approach to managing criminal data with efficient search capabilities. The hybrid C++/Python architecture leverages the strengths of both languages - C++ for performance-critical data operations and Python for rapid GUI development.

The current implementation provides a solid foundation with room for significant enhancements in security, scalability, and user experience. The modular design and clear separation of concerns make it well-positioned for future growth and feature additions.

**Key Strengths**:
- Efficient O(log n) search operations using Red-Black Trees
- Clean separation between GUI and business logic
- Type-safe language integration via CFFI
- Extensible design supporting new crime types and search methods

**Priority Improvements**:
1. Implement user authentication and authorization
2. Add persistent database storage
3. Enhance input validation and security measures
4. Modernize the user interface
5. Add comprehensive logging and audit trails