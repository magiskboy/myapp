import os
import uvicorn
from main.app import create_app

if __name__ == "__main__":
    env = os.getenv("MYAPP_ENV", "production")
    host = os.getenv("MYAPP_HOST", "0.0.0.0"),
    port = int(os.getenv("PORT", "5000"))

    app = create_app(env)
    uvicorn.run(
        app,
        host=host,
        port=port,
    )
