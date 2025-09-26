CC = g++
CFLAGS = -shared -fPIC
OUTPUT = mylib.dll
SRCS = CrimeRecord.cpp Criminal.cpp Person.cpp System.cpp

all: $(OUTPUT)

$(OUTPUT): $(SRCS)
	$(CC) $(CFLAGS) -o $(OUTPUT) $(SRCS)

clean:
	rm -f $(OUTPUT)
