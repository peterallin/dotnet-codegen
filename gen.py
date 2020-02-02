#!/usr/bin/env python3

msg = open("message.txt", "r").read().strip()
code = f"""
using System;

class Generated
{{
    public void deliverMessage()
    {{
        Console.WriteLine("Listen very carefully, I shall say this only once: {msg}");
    }}
}}
"""

open("Generated.cs", "w").write(code)
