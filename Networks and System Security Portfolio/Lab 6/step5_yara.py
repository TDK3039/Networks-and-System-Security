import yara

sample = r"C:\Users\david\OneDrive\Documents\Lab 6\Procmon.exe"

rule_source = """
rule Contains_HTTP{
    strings:
        $http = "http"
        condition:
            $http
}
"""

rules = yara.compile(source=rule_source)
matches = rules.match(sample)

print("The YARA Matches:")
for match in matches:
    print(" -", match.rule)