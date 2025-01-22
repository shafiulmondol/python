#syntex= dir([object])
x=5
my_name='shafiul'
#print(type(x))
#print(dir(x))
print(help("modules")) #for knowing all modules
'''['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', 
'__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', 
'__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
'__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 
'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 
'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 
 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
 no dash is normal method and normal attributes
 but dash is special method and special method
 all attributes and method for string
 '''

'''['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', 
'__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', 
'__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', 
'__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', 
'__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', 
'__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', 
'__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', 
'__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', 
'__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', 
'__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 
'__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 
'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'is_integer', 
'numerator', 'real', 'to_bytes']
all of this for intiger
'''
'''FileHandler         autocommand         marshal             struct
PIL                 backoff             math                subprocess
__future__          backports           mimetypes           sunau
__hello__           base64              mmap                symtable
__phello__          bdb                 mmapfile            sys
_abc                bin                 mmsystem            sysconfig
_aix_support        binascii            modulefinder        tabnanny
_ast                bisect              more_itertools      tarfile
_asyncio            blinker             mouseinfo           telnetlib
_bisect             bool                msilib              tempfile
_blake2             branca              msvcrt              test
_bz2                bs4                 multiprocessing     textwrap
_codecs             buildin_function    netbios             this
_codecs_cn          builtins            netrc               threading
_codecs_hk          bytearry            netutils            time
_codecs_iso2022     bz2                 nntplib             timeit
_codecs_jp          cProfile            nt                  timer
_codecs_kr          calendar            ntpath              tkinter
_codecs_tw          callable            ntsecuritycon       token
_collections        certifi             nturl2path          tokenize
_collections_abc    cgi                 numbers             tomli
_compat_pickle      cgitb               numpy               tomllib
_compression        chardet             odbc                tornado
_contextvars        charset_normalizer  opcode              trace
_csv                chunk               opencage            traceback
_ctypes             click               operator            tracemalloc
_ctypes_test        cmath               optparse            tty
_datetime           cmd                 os                  turtle
_decimal            code                packaging           turtledemo
_distutils_hack     codecs              pathlib             typeguard
_elementtree        codeop              pdb                 types
_functools          collections         perfmon             typing
_hashlib            colorama            phonenumbers        typing_extensions
_heapq              colorsys            pickle              umsgpack
_imp                commctrl            pickletools         unicodedata
_io                 compileall          pip                 unittest
_json               comtypes            pipes               urllib
_locale             concurrent          pkg_resources       urllib3
_lsprof             configparser        pkgutil             uu
_lzma               contextlib          platform            uuid
_markupbase         contextvars         platformdirs        venv
_md5                continuation_charecter plistlib            warnings
_msi                copy                poplib              wave
_multibytecodec     copyreg             posixpath           weakref
_multiprocessing    crypt               pow                 webbrowser
_opcode             csv                 pprint              werkzeug
_operator           ctypes              profile             wheel
_osx_support        curses              pstats              wikipedia
_overlapped         dataclasses         pty                 win2kras
_pickle             datetime            py_compile          win32api
_py_abc             dbConnect           pyautogui           win32clipboard
_pydatetime         dbi                 pyclbr              win32com
_pydecimal          dbm                 pydoc               win32con
_pyio               dde                 pydoc_data          win32console
_pylong             decimal             pyexpat             win32cred
_queue              difflib             pygame              win32crypt
_random             dir                 pygetwindow         win32cryptcon
_sha1               dis                 pylogger            win32event
_sha2               doctest             pymsgbox            win32evtlog
_sha3               email               pyperclip           win32evtlogutil
_signal             encodings           pyrect              win32file
_sitebuiltins       end                 pyscheduler         win32gui
_socket             ensurepip           pyscreeze           win32gui_struct
_sqlite3            enum                pythoncom           win32help
_sre                errno               pyttsx3             win32inet
_ssl                faulthandler        pytweening          win32inetcon
_stat               filecmp             pywhatkit           win32job
_statistics         fileinput           pywin               win32lz
_string             flask               pywin32_bootstrap   win32net
_strptime           fnmatch             pywin32_testutil    win32netcon
_struct             folium              pywintypes          win32pdh
_symtable           fractions           queue               win32pdhquery
_testbuffer         ftplib              quopri              win32pdhutil
_testcapi           functools           random              win32pipe
_testclinic         gc                  rasutil             win32print
_testconsole        genericpath         re                  win32process
_testimportmultiple getopt              referencing         win32profile
_testinternalcapi   getpass             regcheck            win32ras
_testmultiphase     gettext             regutil             win32rcparser
_testsinglephase    glob                reprlib             win32security
_thread             graphlib            requests            win32service
_threading_local    gzip                rlcompleter         win32serviceutil
_tkinter            hashlib             round               win32timezone
_tokenize           heapq               rpds                win32trace
_tracemalloc        hmac                runpy               win32traceutil
_typing             html                sched               win32transaction
_uuid               http                scheduler           win32ts
_warnings           idlelib             secrets             win32ui
_weakref            idna                select              win32uiole
_weakrefset         imaplib             selectors           win32verstamp
_win32sysloader     imghdr              servicemanager      win32wnet
_winapi             importlib           setuptools          winerror
_winxptheme         importlib_metadata  shelve              winioctlcon
_wmi                importlib_resources shlex               winnt
_xxinterpchannels   inflect             shutil              winperf
_xxsubinterpreters  inspect             signal              winreg
_yaml               io                  site                winsound
_zoneinfo           ipaddress           smtplib             winxpgui
abc                 isapi               sndhdr              winxptheme
abs                 itertools           socket              wsgiref
adodbapi            itsdangerous        socketserver        xdrlib
afxres              jinja2              soupsieve           xml
aifc                json                sqlite3             xmlrpc
all                 jsonschema          sre_compile         xxsubtype
antigravity         jsonschema_specifications sre_constants       xyzservices
any                 keyword             sre_parse           yaml
argparse            lib2to3             ssl                 zipapp
array               linecache           sspi                zipfile
ast                 locale              sspicon             zipimport
asyncio             logging             start_pythonwin     zipp
atexit              lzma                stat                zlib
attr                mailbox             statistics          zoneinfo
attrs               mailcap             string
audioop             markupsafe          stringprep

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".
'''