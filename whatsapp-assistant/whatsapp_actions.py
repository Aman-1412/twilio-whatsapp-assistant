#!/usr/bin/env python

def open_chat(num=9876543210):
    if num.startswith("+") and num[1:].isdigit():
        return f"https://wa.me/{num[1:]}"
    if num.isdigit():
        if len(num) > 10:
            return f"https://wa.me/{num}"
        elif len(num) == 10:
            return f"https://wa.me/91{num}"
    return "Provide a correct number"
