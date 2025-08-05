
# tooba se krwaya 
# from seleniumbase import SB
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import os, json, time
# from dotenv import load_dotenv


# def scrape_jobs(title, location):
#     jobs = []
#     with SB(uc=True, test=True, locale="en-US") as sb:
#         sb.open("https://www.linkedin.com/login")
#         time.sleep(10)
#         driver: webdriver.Chrome = sb.driver

#         # Login
#         driver.find_element(By.ID, "username").send_keys(os.getenv("LINKEDIN_EMAIL"))
#         driver.find_element(By.ID, "password").send_keys(os.getenv("LINKEDIN_PASSWORD"))
#         driver.find_element(By.XPATH, "//button[@type='submit']").click()
#         time.sleep(3)
#         input("🔐 Solve CAPTCHA manually and press ENTER to continue...")

#         # Job search
#         search_url = f"https://www.linkedin.com/jobs/search/?keywords={title}&location={location}&f_AL=true"
#         driver.get(search_url)
#         time.sleep(5)

#         job_cards = driver.find_elements(By.CSS_SELECTOR, "div.job-card-container--clickable")

#         for card in job_cards:
#             try:
#                 time.sleep(2)
#                 job_title = card.find_element(By.CSS_SELECTOR, ".visually-hidden").text
#                 company = card.find_element(By.CSS_SELECTOR, ".artdeco-entity-lockup__subtitle").text
#                 job_location = card.find_element(By.CSS_SELECTOR, ".artdeco-entity-lockup__caption").text

#                 jobs.append({"title": job_title, "company": company, "location": job_location})

#                 try:
#                     easy_apply_btn = WebDriverWait(driver, 10).until(
#                         EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button"))
#                     )

#                     if "Easy Apply" in easy_apply_btn.text:
#                         driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", easy_apply_btn)
#                         time.sleep(1)
#                         try:
#                             driver.execute_script("arguments[0].click();", easy_apply_btn)
#                         except:
#                             ActionChains(driver).move_to_element(easy_apply_btn).click().perform()
#                         print(f"✅ Easy Apply clicked for {job_title} at {company}")
#                         time.sleep(2)

#                         # Fill text/tel/email fields
#                         input_fields = driver.find_elements(By.CSS_SELECTOR, "input[type='text'], input[type='tel'], input[type='email']")
#                         for field in input_fields:
#                             label = field.get_attribute("aria-label") or field.get_attribute("placeholder") or ""
#                             value = ""
#                             if "Zip" in label: value = "54000"
#                             elif "Phone" in label: value = "03001234567"

#                             elif "Mobile Number" in label: value = "03001234567"

#                             elif "Email" in label: value = "parizaad60@gmail.com"
#                             # elif "City" in label: value = "Lahore"
#                             elif "Street" in label: value = "Gulberg III"
#                             elif "State" in label: value = "Punjab"
#                             elif "First name" in label: value = "Zaad"
#                             elif "Last name" in label: value = "Khan"
#                             if value:
#                                 try:
#                                     field.clear()
#                                     field.send_keys(value)
                                    
#                                 except:
#                                     continue

#                         # Fill select dropdowns (e.g., country)
#                         try:
#                             next_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Next') or @aria-label='Continue to next step' or //button[contains(text(),'Review')]")
#                             driver.execute_script("arguments[0].click();", next_btn)
#                             print("👉 Clicked Next step")
#                         except Exception as e:
#                             print(e)
#                         selects = driver.find_elements(By.TAG_NAME, "select")
#                         for dropdown in selects:
#                             try:
#                                 Select(dropdown).select_by_visible_text("Pakistan")
#                             except:
#                                 try:
#                                     Select(dropdown).select_by_index(1)
#                                 except:
#                                     continue

#                         # Click radio buttons
#                         radios = driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
#                         for radio in radios:
#                             try:
#                                 driver.execute_script("arguments[0].click();", radio)
#                                 break
#                             except:
#                                 continue

#                         # Salary fields if exist
#                         other_fields = driver.find_elements(By.CSS_SELECTOR, "input[placeholder='']")
#                         for field in other_fields:
#                             ph = field.get_attribute("placeholder")
#                             if ph == "Current salary":
#                                 field.send_keys("100000")
#                             elif ph == "Expected salary":
#                                 field.send_keys("150000")

#                         # Resume upload
#                         try:
#                             upload_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
#                             resume_path = os.path.abspath("Resume.pdf")
#                             if os.path.exists(resume_path):
#                                 upload_input.send_keys(resume_path)
#                         except:
#                             pass

#                         # Step-by-step navigation: Next -> Submit
#                         try:
#                             while True:
#                                 time.sleep(1)
#                                 try:
#                                     next_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Next') or @aria-label='Continue to next step' or //button[contains(text(),'Review')]")
#                                     driver.execute_script("arguments[0].click();", next_btn)
#                                     print("👉 Clicked Next step")
#                                 except:
#                                     try:
#                                         submit_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
#                                         driver.execute_script("arguments[0].click();", submit_btn)
#                                         print("🎯 Submitted Final Application")
#                                         break
#                                     except:
#                                         print("⚠️ No Next or Submit found — maybe already submitted or skipped.")
#                                         break
#                         except Exception as e:
#                             print("❌ Error in step-wise submission:", e)

#                         # Close modal
#                         # try:
#                         #     close_btn = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Dismiss']")
#                         #     driver.execute_script("arguments[0].click();", close_btn)
#                         #     print("❎ Modal closed after apply process")
#                         # except:
#                         #     print("❌ Could not close modal")

#                 except Exception as e:
#                     print(f"No Easy Apply for {job_title}: {e}")

#             except Exception as e:
#                 print(f"Error processing job card: {e}")

#     with open("linkedin_jobs.json", "w") as f:
#         json.dump(jobs, f, indent=2)

# gpt se krwaya 
# from seleniumbase import SB
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import os, json, time
# from dotenv import load_dotenv


# def scrape_jobs(title, location):
#     jobs = []
#     with SB(uc=True, test=True, locale="en-US") as sb:
#         sb.open("https://www.linkedin.com/login")
#         time.sleep(10)
#         driver: webdriver.Chrome = sb.driver

#         # Login
#         driver.find_element(By.ID, "username").send_keys(os.getenv("LINKEDIN_EMAIL"))
#         driver.find_element(By.ID, "password").send_keys(os.getenv("LINKEDIN_PASSWORD"))
#         driver.find_element(By.XPATH, "//button[@type='submit']").click()
#         time.sleep(3)
#         input("🔐 Solve CAPTCHA manually and press ENTER to continue...")

#         # Job search
#         search_url = f"https://www.linkedin.com/jobs/search/?keywords={title}&location={location}&f_AL=true"
#         driver.get(search_url)
#         time.sleep(5)

#         job_cards = driver.find_elements(By.CSS_SELECTOR, "div.job-card-container--clickable")

#         for card in job_cards:
#             try:
#                 time.sleep(2)
#                 job_title = card.find_element(By.CSS_SELECTOR, ".visually-hidden").text
#                 company = card.find_element(By.CSS_SELECTOR, ".artdeco-entity-lockup__subtitle").text
#                 job_location = card.find_element(By.CSS_SELECTOR, ".artdeco-entity-lockup__caption").text

#                 jobs.append({"title": job_title, "company": company, "location": job_location})

#                 try:
#                     easy_apply_btn = WebDriverWait(driver, 10).until(
#                         EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button"))
#                     )

#                     if "Easy Apply" in easy_apply_btn.text:
#                         driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", easy_apply_btn)
#                         time.sleep(1)
#                         try:
#                             driver.execute_script("arguments[0].click();", easy_apply_btn)
#                         except:
#                             ActionChains(driver).move_to_element(easy_apply_btn).click().perform()
#                         print(f"✅ Easy Apply clicked for {job_title} at {company}")
#                         time.sleep(2)

#                         # Fill input fields
#                         input_fields = driver.find_elements(By.CSS_SELECTOR, "input")
#                         for field in input_fields:
#                             label = field.get_attribute("aria-label") or field.get_attribute("placeholder") or ""
#                             field_type = field.get_attribute("type")
#                             value = ""

#                             if "zip" in label.lower(): value = "54000"
#                             elif "phone" in label.lower(): value = "03001234567"
#                             elif "email" in label.lower(): value = "parizaad60@gmail.com"
#                             elif "street" in label.lower(): value = "Gulberg III"
#                             elif "state" in label.lower(): value = "Punjab"
#                             elif "first name" in label.lower(): value = "Zaad"
#                             elif "last name" in label.lower(): value = "Khan"
#                             elif "years" in label.lower(): value = "2"
#                             elif field_type == "number": value = "2"

#                             if value:
#                                 try:
#                                     field.clear()
#                                     field.send_keys(value)
#                                 except:
#                                     continue

#                         # Handle dynamic question blocks
#                         try:
#                             question_blocks = driver.find_elements(By.XPATH, "//fieldset[contains(@class, 'artdeco-field')]")
#                             for block in question_blocks:
#                                 try:
#                                     label_text = block.text.lower()

#                                     # Dropdown handling
#                                     if "select an option" in label_text or "proficiency" in label_text:
#                                         dropdown = block.find_element(By.TAG_NAME, "select")
#                                         Select(dropdown).select_by_index(1)

#                                     # Numeric inputs
#                                     if any(x in label_text for x in ["how many years", "experience", "python", "jupyter", "machine learning"]):
#                                         inputs = block.find_elements(By.TAG_NAME, "input")
#                                         for input_box in inputs:
#                                             if input_box.get_attribute("type") == "number":
#                                                 input_box.clear()
#                                                 input_box.send_keys("2")

#                                     # Yes/No radio buttons
#                                     radio_labels = block.find_elements(By.XPATH, ".//label")
#                                     for radio_label in radio_labels:
#                                         radio_text = radio_label.text.strip().lower()
#                                         if radio_text in ["yes", "no"]:
#                                             if "comfortable" in label_text or "education" in label_text:
#                                                 if "yes" in radio_text:
#                                                     radio_input = radio_label.find_element(By.XPATH, ".//preceding-sibling::input[@type='radio']")
#                                                     driver.execute_script("arguments[0].click();", radio_input)
#                                                     break

#                                 except Exception as block_error:
#                                     print("⚠️ Error processing block:", block_error)

#                         except Exception as e:
#                             print("⚠️ Error handling dynamic questions:", e)

#                         # Select country dropdowns
#                         selects = driver.find_elements(By.TAG_NAME, "select")
#                         for dropdown in selects:
#                             try:
#                                 Select(dropdown).select_by_visible_text("Pakistan")
#                             except:
#                                 try:
#                                     Select(dropdown).select_by_index(1)
#                                 except:
#                                     continue

#                         # Resume upload
#                         try:
#                             upload_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
#                             resume_path = os.path.abspath("Resume.pdf")
#                             if os.path.exists(resume_path):
#                                 upload_input.send_keys(resume_path)
#                         except:
#                             pass

#                         # Navigation steps
#                         try:
#                             step_count = 0
#                             while step_count < 15:
#                                 time.sleep(1)
#                                 step_count += 1
#                                 try:
#                                     next_btn = WebDriverWait(driver, 3).until(
#                                         EC.element_to_be_clickable((By.XPATH,
#                                             "//button[contains(text(),'Next')] | //button[contains(text(),'Review')] | //button[@aria-label='Continue to next step']"))
#                                     )
#                                     if next_btn.is_enabled():
#                                         driver.execute_script("arguments[0].scrollIntoView();", next_btn)
#                                         driver.execute_script("arguments[0].click();", next_btn)
#                                         print("👉 Clicked Next/Review step")
#                                     else:
#                                         print("⚠️ Next button is disabled — missing required input")
#                                         break
#                                 except:
#                                     try:
#                                         submit_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Submit')]")
#                                         driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
#                                         driver.execute_script("arguments[0].click();", submit_btn)
#                                         print("🎯 Submitted Final Application")
#                                         break
#                                     except:
#                                         print("⚠️ No Next or Submit found — maybe already submitted or skipped.")
#                                         break
#                         except Exception as e:
#                             print("❌ Error in step-wise submission:", e)

#                 except Exception as e:
#                     print(f"No Easy Apply for {job_title}: {e}")

#             except Exception as e:
#                 print(f"Error processing job card: {e}")

#     with open("linkedin_jobs.json", "w") as f:
#         json.dump(jobs, f, indent=2)
# from seleniumbase import SB
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import os, json, time
# from dotenv import load_dotenv
# import openai
# from utils import extract_content, save_cover_letter_to_pdf, log_application

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# resume_text = extract_content("Resume.pdf")

# def get_answer_from_gpt(question, resume_text):
#     try:
#         prompt = f"""
#         Question: "{question}"
#         Resume: "{resume_text}"
#         Based on the resume, provide the best possible answer. If Yes/No type, just respond 'Yes' or 'No'.
#         """
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are an expert HR assistant that provides short and accurate answers for job application questions."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         print("❌ GPT error:", e)
#         return ""

# def scrape_jobs(title, location):
#     jobs = []
#     with SB(uc=True, test=True, locale="en-US") as sb:
#         sb.open("https://www.linkedin.com/login")
#         time.sleep(10)
#         driver: webdriver.Chrome = sb.driver

#         driver.find_element(By.ID, "username").send_keys(os.getenv("LINKEDIN_EMAIL"))
#         driver.find_element(By.ID, "password").send_keys(os.getenv("LINKEDIN_PASSWORD"))
#         driver.find_element(By.XPATH, "//button[@type='submit']").click()
#         time.sleep(3)
#         input("🔐 Solve CAPTCHA manually and press ENTER to continue...")

#         search_url = f"https://www.linkedin.com/jobs/search/?keywords={title}&location={location}&f_AL=true"
#         driver.get(search_url)
#         time.sleep(5)

#         job_cards = driver.find_elements(By.CSS_SELECTOR, "div.job-card-container--clickable")

#         for card in job_cards:
#             try:
#                 time.sleep(2)
#                 job_title = card.find_element(By.CSS_SELECTOR, ".visually-hidden").text
#                 company = card.find_element(By.CSS_SELECTOR, ".artdeco-entity-lockup__subtitle").text
#                 job_location = card.find_element(By.CSS_SELECTOR, ".artdeco-entity-lockup__caption").text

#                 jobs.append({"title": job_title, "company": company, "location": job_location})

#                 try:
#                     easy_apply_btn = WebDriverWait(driver, 10).until(
#                         EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button"))
#                     )

#                     if "Easy Apply" in easy_apply_btn.text:
#                         driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", easy_apply_btn)
#                         time.sleep(1)
#                         try:
#                             driver.execute_script("arguments[0].click();", easy_apply_btn)
#                         except:
#                             ActionChains(driver).move_to_element(easy_apply_btn).click().perform()
#                         print(f"✅ Easy Apply clicked for {job_title} at {company}")
#                         time.sleep(2)

#                         input_fields = driver.find_elements(By.CSS_SELECTOR, "input")
#                         for field in input_fields:
#                             label = field.get_attribute("aria-label") or field.get_attribute("placeholder") or ""
#                             field_type = field.get_attribute("type")
#                             value = ""

#                             if "zip" in label.lower(): value = "54000"
#                             elif "phone" in label.lower(): value = "03001234567"
#                             elif "email" in label.lower(): value = "parizaad60@gmail.com"
#                             elif "street" in label.lower(): value = "Gulberg III"
#                             elif "state" in label.lower(): value = "Punjab"
#                             elif "first name" in label.lower(): value = "Zaad"
#                             elif "last name" in label.lower(): value = "Khan"
#                             elif "years" in label.lower(): value = "2"
#                             elif field_type == "number": value = "2"

#                             if value:
#                                 try:
#                                     field.clear()
#                                     field.send_keys(value)
#                                 except:
#                                     continue

#                         try:
#                             form_blocks = driver.find_elements(By.XPATH, "//fieldset[contains(@class, 'artdeco-field')]")
#                             for block in form_blocks:
#                                 label_text = block.text.strip()
#                                 gpt_answer = get_answer_from_gpt(label_text, resume_text)

#                                 try:
#                                     select_el = block.find_element(By.TAG_NAME, "select")
#                                     Select(select_el).select_by_visible_text(gpt_answer)
#                                     continue
#                                 except:
#                                     pass

#                                 try:
#                                     numeric_inputs = block.find_elements(By.TAG_NAME, "input")
#                                     for inp in numeric_inputs:
#                                         if inp.get_attribute("type") == "number":
#                                             inp.clear()
#                                             inp.send_keys(gpt_answer)
#                                             break
#                                 except:
#                                     pass

#                                 try:
#                                     radios = block.find_elements(By.XPATH, ".//input[@type='radio']")
#                                     for radio in radios:
#                                         try:
#                                             label_element = radio.find_element(By.XPATH, "./following-sibling::*[contains(@class, 't-14')]")
#                                             label_text = label_element.text.strip().lower()
#                                             if gpt_answer.lower() in label_text:
#                                                 driver.execute_script("arguments[0].click();", radio)
#                                                 print(f"✅ Selected radio with class t-14: {label_text}")
#                                                 break
#                                         except:
#                                             continue
#                                 except Exception as e:
#                                     print("⚠️ Radio button click failed:", e)

#                         except Exception as e:
#                             print("⚠️ Error in dynamic question handling:", e)

#                         try:
#                             upload_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
#                             resume_path = os.path.abspath("Resume.pdf")
#                             if os.path.exists(resume_path):
#                                 upload_input.send_keys(resume_path)
#                         except:
#                             pass

#                         try:
#                             step_count = 0
#                             while step_count < 15:
#                                 time.sleep(1)
#                                 step_count += 1
#                                 try:
#                                     nav_btn = WebDriverWait(driver, 3).until(
#                                         EC.element_to_be_clickable((By.XPATH,
#                                             "//button[contains(text(),'Next')] | //button[contains(text(),'Review')] | //button[contains(text(),'Submit')] | //button[@aria-label='Continue to next step'] | //button[@data-control-name='continue_unify']"))
#                                     )
#                                     if nav_btn.is_enabled():
#                                         driver.execute_script("arguments[0].scrollIntoView();", nav_btn)
#                                         driver.execute_script("arguments[0].click();", nav_btn)
#                                         print("👉 Clicked Next/Review/Submit step")
#                                     else:
#                                         print("⚠️ Navigation button is disabled — missing required input")
#                                         break
#                                 except:
#                                     print("⚠️ No valid navigation button found — maybe already submitted or skipped.")
#                                     break
#                         except Exception as e:
#                             print("❌ Error in step-wise submission:", e)

#                 except Exception as e:
#                     print(f"No Easy Apply for {job_title}: {e}")

#             except Exception as e:
#                 print(f"Error processing job card: {e}")

#     with open("linkedin_jobs.json", "w") as f:
#         json.dump(jobs, f, indent=2)

# from seleniumbase import SB
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait, Select
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# import os, json, time
# from dotenv import load_dotenv
# import openai
# from utils import extract_content, save_cover_letter_to_pdf, log_application

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# resume_text = extract_content("Resume.pdf")

# def get_answer_from_gpt(question, resume_text):
#     try:
#         prompt = f"""
#         Question: "{question}"
#         Resume: "{resume_text}"
#         Based on the resume, provide the best possible answer. If Yes/No type, just respond 'Yes' or 'No'.
#         """
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are an expert HR assistant that provides short and accurate answers for job application questions."},
#                 {"role": "user", "content": prompt}
#             ]
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         print("❌ GPT error:", e)
#         return ""

# def scrape_jobs(title, location):
#     jobs = []
#     with SB(uc=True, test=True, locale="en-US") as sb:
#         sb.open("https://www.linkedin.com/login")
#         time.sleep(10)
#         driver: webdriver.Chrome = sb.driver

#         driver.find_element(By.ID, "username").send_keys(os.getenv("LINKEDIN_EMAIL"))
#         driver.find_element(By.ID, "password").send_keys(os.getenv("LINKEDIN_PASSWORD"))
#         driver.find_element(By.XPATH, "//button[@type='submit']").click()
#         time.sleep(3)
#         input("🔐 Solve CAPTCHA manually and press ENTER to continue...")

#         search_url = f"https://www.linkedin.com/jobs/search/?keywords={title}&location={location}&f_AL=true"
#         driver.get(search_url)
#         time.sleep(5)

#         job_cards = driver.find_elements(By.CSS_SELECTOR, "div.job-card-container--clickable")

#         for card in job_cards:
#             try:
#                 time.sleep(2)
#                 job_title = card.find_element(By.CSS_SELECTOR, ".visually-hidden").text
#                 company = card.find_element(By.CSS_SELECTOR, ".artdeco-entity-lockup__subtitle").text
#                 job_location = card.find_element(By.CSS_SELECTOR, ".artdeco-entity-lockup__caption").text

#                 jobs.append({"title": job_title, "company": company, "location": job_location})

#                 try:
#                     easy_apply_btn = WebDriverWait(driver, 10).until(
#                         EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button"))
#                     )

#                     if "Easy Apply" in easy_apply_btn.text:
#                         driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", easy_apply_btn)
#                         time.sleep(1)
#                         try:
#                             driver.execute_script("arguments[0].click();", easy_apply_btn)
#                         except:
#                             ActionChains(driver).move_to_element(easy_apply_btn).click().perform()
#                         print(f"✅ Easy Apply clicked for {job_title} at {company}")
#                         time.sleep(2)

#                         input_fields = driver.find_elements(By.CSS_SELECTOR, "input")
#                         for field in input_fields:
#                             label = field.get_attribute("aria-label") or field.get_attribute("placeholder") or ""
#                             field_type = field.get_attribute("type")
#                             value = ""

#                             if "zip" in label.lower(): value = "54000"
#                             elif "phone" in label.lower(): value = "03001234567"
#                             elif "email" in label.lower(): value = "alexander.landaverde01@gmail.com"
#                             elif "street" in label.lower(): value = "USA "
#                             elif "state" in label.lower(): value = "Dallas"
#                             elif "first name" in label.lower(): value = "Alexander"
#                             elif "last name" in label.lower(): value = "Lavender"
#                             elif "years" in label.lower(): value = "2"
#                             elif field_type == "number": value = "2"

#                             if value:
#                                 try:
#                                     field.clear()
#                                     field.send_keys(value)
#                                 except:
#                                     continue

#                         try:
#                             form_blocks = driver.find_elements(By.XPATH, "//fieldset[contains(@class, 'artdeco-field')]")
#                             for block in form_blocks:
#                                 label_text = block.text.strip()
#                                 gpt_answer = get_answer_from_gpt(label_text, resume_text)

#                                 try:
#                                     select_el = block.find_element(By.TAG_NAME, "select")
#                                     Select(select_el).select_by_visible_text(gpt_answer)
#                                     continue
#                                 except:
#                                     pass

#                                 try:
#                                     numeric_inputs = block.find_elements(By.TAG_NAME, "input")
#                                     for inp in numeric_inputs:
#                                         if inp.get_attribute("type") == "number":
#                                             inp.clear()
#                                             inp.send_keys(gpt_answer)
#                                             break
#                                 except:
#                                     pass

#                                 try:
#                                     radios = block.find_elements(By.XPATH, ".//input[@type='radio']")
#                                     for radio in radios:
#                                         try:
#                                             label_element = radio.find_element(By.XPATH, "./following-sibling::*[contains(@class, 't-14')]")
#                                             label_text = label_element.text.strip().lower()
#                                             if gpt_answer.lower() in label_text:
#                                                 driver.execute_script("arguments[0].click();", radio)
#                                                 print(f"✅ Selected radio with class t-14: {label_text}")
#                                                 break
#                                         except:
#                                             continue
#                                 except Exception as e:
#                                     print("⚠️ Radio button click failed:", e)

#                         except Exception as e:
#                             print("⚠️ Error in dynamic question handling:", e)

#                         try:
#                             upload_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
#                             resume_path = os.path.abspath("Resume.pdf")
#                             if os.path.exists(resume_path):
#                                 upload_input.send_keys(resume_path)
#                         except:
#                             pass

#                         try:
#                             step_count = 0
#                             while step_count < 15:
#                                 time.sleep(1)
#                                 step_count += 1
#                                 try:
#                                     nav_btn = WebDriverWait(driver, 3).until(
#                                         EC.element_to_be_clickable((By.XPATH,
#                                             "//button[contains(text(),'Next')] | //button[contains(text(),'Review')] | //button[contains(text(),'Submit')] | //button[@aria-label='Continue to next step'] | //button[@data-control-name='continue_unify'] | //button[.//span[contains(@class, 'artdeco-button__text') and text()='Review']]")
#                                     ))
#                                     if nav_btn.is_enabled():
#                                         driver.execute_script("arguments[0].scrollIntoView();", nav_btn)
#                                         driver.execute_script("arguments[0].click();", nav_btn)
#                                         print("👉 Clicked Next/Review/Submit step")
#                                     else:
#                                         print("⚠️ Navigation button is disabled — missing required input")
#                                         break
#                                 except:
#                                     print("⚠️ No valid navigation button found — maybe already submitted or skipped.")
#                                     break
#                         except Exception as e:
#                             print("❌ Error in step-wise submission:", e)

#                 except Exception as e:
#                     print(f"No Easy Apply for {job_title}: {e}")

#             except Exception as e:
#                 print(f"Error processing job card: {e}")

#     with open("linkedin_jobs.json", "w") as f:
#         json.dump(jobs, f, indent=2)




from seleniumbase import SB
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os, json, time
from utils import extract_content, save_cover_letter_to_pdf, log_application
import openai

# 🔐 Direct login credentials (replace with yours safely for testing only)
LINKEDIN_EMAIL = "alexander.landaverde01@gmail.com"
LINKEDIN_PASSWORD = "Lx052736512_"

# LINKEDIN_EMAIL = "parizaad60@gmail.com"
# LINKEDIN_PASSWORD = "Wav06529"

# 🔑 OpenAI API Key
openai.api_key = "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"

resume_text = extract_content("Resume.pdf")

def get_answer_from_gpt(question, resume_text):
    try:
        prompt = f"""
        Question: "{question}"
        Resume: "{resume_text}"
        Based on the resume, provide the best possible answer. If Yes/No type, just respond 'Yes' or 'No'.
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert HR assistant that provides short and accurate answers for job application questions."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("❌ GPT error:", e)
        return ""

def scrape_jobs(title, location):
    jobs = []
    with SB(uc=True, test=True, locale="en-US") as sb:
        sb.open("https://www.linkedin.com/login")
        time.sleep(10)
        driver: webdriver.Chrome = sb.driver

        driver.find_element(By.ID, "username").send_keys(LINKEDIN_EMAIL)
        driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        input("🔐 Solve CAPTCHA manually and press ENTER to continue...")

        search_url = f"https://www.linkedin.com/jobs/search/?keywords={title}&location={location}&f_AL=true"
        driver.get(search_url)
        time.sleep(5)

        job_cards = driver.find_elements(By.CSS_SELECTOR, "div.job-card-container--clickable")

        for card in job_cards:
            try:
                time.sleep(2)
                job_title = card.find_element(By.CSS_SELECTOR, ".visually-hidden").text
                company = card.find_element(By.CSS_SELECTOR, ".artdeco-entity-lockup__subtitle").text
                job_location = card.find_element(By.CSS_SELECTOR, ".artdeco-entity-lockup__caption").text

                jobs.append({"title": job_title, "company": company, "location": job_location})

                try:
                    easy_apply_btn = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, ".jobs-apply-button"))
                    )

                    if "Easy Apply" in easy_apply_btn.text:
                        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", easy_apply_btn)
                        time.sleep(1)
                        try:
                            driver.execute_script("arguments[0].click();", easy_apply_btn)
                        except:
                            ActionChains(driver).move_to_element(easy_apply_btn).click().perform()
                        print(f"✅ Easy Apply clicked for {job_title} at {company}")
                        time.sleep(2)

                        input_fields = driver.find_elements(By.CSS_SELECTOR, "input")
                        for field in input_fields:
                            label = field.get_attribute("aria-label") or field.get_attribute("placeholder") or ""
                            field_type = field.get_attribute("type")
                            value = ""

                            if "zip" in label.lower(): value = "54000"
                            elif "phone" in label.lower(): value = "030123456789"
                            elif "email" in label.lower(): value = LINKEDIN_EMAIL
                            elif "street" in label.lower(): value = " USA"
                            elif "state" in label.lower(): value = "Dallas"
                            elif "first name" in label.lower(): value = "Alexander"
                            elif "last name" in label.lower(): value = "Lavendar"
                            elif "years" in label.lower(): value = "2"
                            elif field_type == "number": value = "2"

                            if value:
                                try:
                                    field.clear()
                                    field.send_keys(value)
                                except:
                                    continue

                        try:
                            form_blocks = driver.find_elements(By.XPATH, "//fieldset[contains(@class, 'artdeco-field')]")
                            for block in form_blocks:
                                label_text = block.text.strip()
                                gpt_answer = get_answer_from_gpt(label_text, resume_text)

                                try:
                                    select_el = block.find_element(By.TAG_NAME, "select")
                                    Select(select_el).select_by_visible_text(gpt_answer)
                                    continue
                                except:
                                    pass

                                try:
                                    numeric_inputs = block.find_elements(By.TAG_NAME, "input")
                                    for inp in numeric_inputs:
                                        if inp.get_attribute("type") == "number":
                                            inp.clear()
                                            inp.send_keys(gpt_answer)
                                            break
                                except:
                                    pass

                                try:
                                    radios = block.find_elements(By.XPATH, ".//input[@type='radio']")
                                    for radio in radios:
                                        try:
                                            label_element = radio.find_element(By.XPATH, "./following-sibling::*[contains(@class, 't-14')]")
                                            label_text = label_element.text.strip().lower()
                                            if gpt_answer.lower() in label_text:
                                                driver.execute_script("arguments[0].click();", radio)
                                                print(f"✅ Selected radio with class t-14: {label_text}")
                                                break
                                        except:
                                            continue
                                except Exception as e:
                                    print("⚠️ Radio button click failed:", e)

                        except Exception as e:
                            print("⚠️ Error in dynamic question handling:", e)

                        try:
                            upload_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
                            resume_path = os.path.abspath("Resume.pdf")
                            if os.path.exists(resume_path):
                                upload_input.send_keys(resume_path)
                        except:
                            pass

                        try:
                            step_count = 0
                            while step_count < 15:
                                time.sleep(1)
                                step_count += 1
                                try:
                                    nav_btn = WebDriverWait(driver, 3).until(
                                        EC.element_to_be_clickable((By.XPATH,
                                            "//button[contains(text(),'Next')] | //button[contains(text(),'Review')] | //button[contains(text(),'Submit')] | //button[@aria-label='Continue to next step'] | //button[@data-control-name='continue_unify'] | //button[.//span[contains(@class, 'artdeco-button__text') and text()='Review']]")
                                    ))
                                    if nav_btn.is_enabled():
                                        driver.execute_script("arguments[0].scrollIntoView();", nav_btn)
                                        driver.execute_script("arguments[0].click();", nav_btn)
                                        print("👉 Clicked Next/Review/Submit step")
                                    else:
                                        print("⚠️ Navigation button is disabled — missing required input")
                                        break
                                except:
                                    print("⚠️ No valid navigation button found — maybe already submitted or skipped.")
                                    break
                        except Exception as e:
                            print("❌ Error in step-wise submission:", e)

                except Exception as e:
                    print(f"No Easy Apply for {job_title}: {e}")

            except Exception as e:
                print(f"Error processing job card: {e}")

    with open("linkedin_jobs.json", "w") as f:
        json.dump(jobs, f, indent=2)
