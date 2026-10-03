from fastapi import FastAPI
import asyncio
from dashboard import bot_state, start_web_dashboard

app = FastAPI()

from bot import main as bot_main, cb_login_only, cb_set_target, cb_start_account, \
    cb_stop_account, cb_halt_account, cb_delete_account, cb_add_friend, \
    cb_generate_accounts, cb_gen_start, cb_gen_import

_bot_started = False

@app.on_event("startup")
async def startup():
    global _bot_started
    if _bot_started:
        return
    _bot_started = True
    bot_state.bind_loop()
    bot_state.refresh_callbacks["on_account_login_only"] = cb_login_only
    bot_state.refresh_callbacks["on_set_target"] = cb_set_target
    bot_state.refresh_callbacks["on_start_account"] = cb_start_account
    bot_state.refresh_callbacks["on_stop_account"] = cb_stop_account
    bot_state.refresh_callbacks["on_halt_account"] = cb_halt_account
    bot_state.refresh_callbacks["on_delete_account"] = cb_delete_account
    bot_state.refresh_callbacks["on_add_friend"] = cb_add_friend
    bot_state.refresh_callbacks["on_generate_accounts"] = cb_generate_accounts
    bot_state.refresh_callbacks["on_gen_start"] = cb_gen_start
    bot_state.refresh_callbacks["on_gen_import"] = cb_gen_import

@app.get("/")
def root():
    return {"status": "bot running"}
