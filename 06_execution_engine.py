# Cell 6: The Main Execution Engine (Improved Logging)

def run_turn(user_message):
    print("\n" + "=" * 60)
    print(f"👤 USER: {user_message}")
    print("-" * 60)
    
    response = send_message_safe(user_message)
    if not response: return 

    # Loop to handle Tool Calls
    while response.candidates and response.candidates[0].content.parts:
        part = response.candidates[0].content.parts[0]
        
        if part.function_call:
            fc = part.function_call
            fname = fc.name
            fargs = {k: v for k, v in fc.args.items()}
            
            print(f"🔧 CALLING TOOL: {fname}")
            
            # Execute Logic
            result = {}
            try:
                if fname == "get_carbon_intensity": result = get_carbon_intensity()
                elif fname == "get_carbon_forecast": result = get_carbon_forecast(**fargs)
                elif fname == "find_greenest_window": result = find_greenest_window(**fargs)
                elif fname == "deploy_task": result = deploy_task(**fargs)
                elif fname == "get_deployment_stats": result = get_deployment_stats()
                else: result = {"error": "Unknown Tool"}
            except Exception as e:
                result = {"error": str(e)}
            
            # Force result to Dict for safety
            if not isinstance(result, dict): result = {"output": str(result)}

            print(f"   ► Result: {str(result)[:100]}...") 
            
            # Send result back
            response = send_message_safe(
                Part(function_response=FunctionResponse(name=fname, response=result))
            )
        else:
            break
            
    # Print Final Response
    try:
        # Check if text exists safely
        if response.text:
            print(f"\n🤖 GREENOPS AGENT: {response.text}")
    except ValueError:
        # This handles the case where the model output is blocked or empty
        print("\n🤖 GREENOPS AGENT: [Action Completed. Check Dashboard.]")
        
    print("=" * 60)

print("✅ Execution Engine Updated.")