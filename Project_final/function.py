import pygame

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

# color
WHITE       =   (255, 255, 255)
BLACK       =   (0, 0, 0)
GRAY        =   (128, 128, 128)
LIGHT_GRAY  =   (200, 200, 200)
BLUE        =   (80, 105, 155)
LIGHT_BLUE  =   (173, 216, 230)
PURPLE      =   (128, 0, 128)
LIGHT_PURPLE=   (230, 120, 230)
RED         =   (205, 0, 0)
LIGHT_RED   =   (255, 50, 50)

# 初始化
pygame.init()
pygame.mixer.init()
pygame.font.init()

# load window surface
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Crime Manager')

# Draw a image that is transparent
def blit_alpha(target, source, location, opacity): # window 圖片 位置 透明度
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, ( -x, - y ))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)        
    target.blit(temp, location)



import cffi

ffi = cffi.FFI()

ffi.cdef("""
         int main(void);
""")

# 定義與 C++ 函數相符的接口
ffi.cdef("""
    void newCriminal(char* criminalType, char* description, int year, int month, int day, int hour, int minute, char* id, char* bir, char* gen, char* loc, char* name);
""")

ffi.cdef("""
    void deleteCriminal(char* name, int year, int month, int day, int hour, int minute);
""")

ffi.cdef("""
    int searchbyTime(int year, int month, int day, int hour, int minute, char** array, int row, int col);
""")

ffi.cdef("""
    int searchbyIntervalTime(int year1, int month1, int day1, int hour1, int minute1, int year2, int month2, int day2, int hour2, int minute2, char** array, int row, int col);
""")

ffi.cdef("""
    int searchbyTimeCrime(int year, int month, int day, int hour, int minute, char* type, char** array, int row, int col);
""")

ffi.cdef("""
    int searchbyIntervalTimeCrime(int year1, int month1, int day1, int hour1, int minute1, int year2, int month2, int day2, int hour2, int minute2, char* type, char** array, int row, int col);
""")

ffi.cdef("""
    int searchbyName(char* name, char** array, int row, int col);
""")


# 加載共享庫
SYSTEM = ffi.dlopen('mylib.dll')

recordNumber = 0    # the number of crimes that committed by the ciminal 
row = 100           # result array size
col = 100
responce = []       # result array

for i in range(row):
    line = ffi.new(f"char[{col}]")  # size of each line
    responce.append(line)

# 創建二維指針陣列
responce_ptr = ffi.new(f"char*[{row}]", responce)    # result array pointer