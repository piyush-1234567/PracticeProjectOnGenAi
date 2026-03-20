def promptBuilder(context,query):
    prompt = f"""
            instructions: you are a string question answering system
            1. Answer only using the provided context
            2. if the answer is not in the context, say i don't know
            3. do not make up the information
            4. keep the answer concise
            Context = {context},
            Query = {query}

            """
    return prompt