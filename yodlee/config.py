import os

RETRIES = int(os.getenv('YODLEE_RETRIES', 5))
RETRY_SLEEP = float(os.getenv('YODLEE_RETRY_SLEEP', 0.5))

FASTLINK_HTML = '''
<form action='{url}' method='post' id='fastlink' style='display: none;'>
    <input name='rsession' value='{rsession}'>
    <input name='app' value='{app}'>
    <input name='redirectReq' value='{redirect}'>
    <input name='token' value='{token}'>
    <input name='extraParams' value='{extra_params}'/>
</form>
<script>
    document.getElementById('fastlink').submit()
</script>'''
