li = ["Larry", "Curly"]
print li.pop
print getattr(li, "pop")
getattr(li, "append")("Moe")
print li
print getattr({}, "clear")
print getattr((), "pop")
