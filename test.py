from aip import AipSpeech

APP_ID = '16881670'
API_KEY = '8FwqrzKk0EAZUWdSol8WHT0p'
SECRET_KEY = 'KhIXWDLGISiWLi2XC2VPt4aX5pHCbWOw'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

result = client.asr(get_file_content('out.pcm'), 'pcm', 16000, {
    'dev_pid': 1537,
})

print(result)

