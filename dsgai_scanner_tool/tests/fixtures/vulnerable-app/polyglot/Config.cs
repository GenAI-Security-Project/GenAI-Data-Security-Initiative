// Fixture C# config — INTENTIONALLY VULNERABLE. Fake value. Never deploy.
using Microsoft.SemanticKernel;
public static class Config {
    // DSGAI02 FAIL — hardcoded raw token (P02.9). Fake value.
    public const string ApiKey = "sk-proj-FAKE00000000000000000000000000";
}
