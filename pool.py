with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
  results = [executor.submit(run_profile, profile) for profile in num]   
