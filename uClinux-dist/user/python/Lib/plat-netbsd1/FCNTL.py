# Generated by h2py from /usr/include/fcntl.h

# Included from sys/types.h

# Included from machine/types.h

# Included from sys/cdefs.h

# Included from machine/cdefs.h
def __P(protos): return protos		 

def __STRING(x): return #x

def __P(protos): return ()		 

def __STRING(x): return "x"

def __attribute__(x): return  

def __kprintf_attribute__(a): return __attribute__(a)


# Included from machine/ansi.h
_BSD_PTRDIFF_T_ = int
_BSD_SSIZE_T_ = int
_BSD_TIME_T_ = long
_BSD_CLOCKID_T_ = int
_BSD_TIMER_T_ = int
_BSD_WCHAR_T_ = int
_BSD_WINT_T_ = int
_BSD_RUNE_T_ = int

# Included from machine/endian.h
_QUAD_HIGHWORD = 1
_QUAD_LOWWORD = 0
LITTLE_ENDIAN = 1234
BIG_ENDIAN = 4321
PDP_ENDIAN = 3412
BYTE_ORDER = LITTLE_ENDIAN
def __byte_swap_long_variable(x): return \

def __byte_swap_long_variable(x): return \

def __byte_swap_word_variable(x): return \

def __byte_swap_long_constant(x): return \

def __byte_swap_word_constant(x): return \

def __byte_swap_long(x): return \

def __byte_swap_word(x): return \

def __byte_swap_long(x): return __byte_swap_long_variable(x)

def __byte_swap_word(x): return __byte_swap_word_variable(x)

def ntohl(x): return __byte_swap_long(x)

def ntohs(x): return __byte_swap_word(x)

def htonl(x): return __byte_swap_long(x)

def htons(x): return __byte_swap_word(x)

def major(x): return ((int32_t)(((u_int32_t)(x) >> 8) & 0xff))

def minor(x): return ((int32_t)((x) & 0xff))

NBBY = 8
FD_SETSIZE = 256
O_RDONLY = 0x0000
O_WRONLY = 0x0001
O_RDWR = 0x0002
O_ACCMODE = 0x0003
FREAD = 0x0001
FWRITE = 0x0002
O_NONBLOCK = 0x0004
O_APPEND = 0x0008
O_SHLOCK = 0x0010
O_EXLOCK = 0x0020
O_ASYNC = 0x0040
O_FSYNC = 0x0080
O_CREAT = 0x0200
O_TRUNC = 0x0400
O_EXCL = 0x0800
FMARK = 0x1000
FDEFER = 0x2000
FHASLOCK = 0x4000
O_NOCTTY = 0
def FFLAGS(oflags): return ((oflags) + 1)

def OFLAGS(fflags): return ((fflags) - 1)

FAPPEND = O_APPEND
FASYNC = O_ASYNC
FFSYNC = O_FSYNC
FNONBLOCK = O_NONBLOCK
FNDELAY = O_NONBLOCK
O_NDELAY = O_NONBLOCK
F_DUPFD = 0
F_GETFD = 1
F_SETFD = 2
F_GETFL = 3
F_SETFL = 4
F_GETOWN = 5
F_SETOWN = 6
F_GETLK = 7
F_SETLK = 8
F_SETLKW = 9
FD_CLOEXEC = 1
F_RDLCK = 1
F_UNLCK = 2
F_WRLCK = 3
F_WAIT = 0x010
F_FLOCK = 0x020
F_POSIX = 0x040
LOCK_SH = 0x01
LOCK_EX = 0x02
LOCK_NB = 0x04
LOCK_UN = 0x08
