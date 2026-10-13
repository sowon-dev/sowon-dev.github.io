const Hexo = require('hexo');

async function main() {
    const hexo = new Hexo(process.cwd(), {});
    hexo.env.init = true;
    
    console.log("1. Initializing Hexo...");
    await hexo.init();
    
    console.log("2. Loading plugins & posts...");
    await hexo.load();
    
    console.log("3. Cleaning previous build...");
    await hexo.call('clean', {});
    
    console.log("4. Generating site files...");
    await hexo.call('generate', {});
    
    console.log("=== FULL_BUILD_COMPLETED_SUCCESSFULLY ===");
}

main().catch(err => {
    console.error("BUILD_FAILED:", err);
    process.exit(1);
});
