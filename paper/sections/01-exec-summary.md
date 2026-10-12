## Executive summary

**What an agent is.** An AI agent is software in which a language model decides, step by step, what to do next. It chooses which tools to call (search, email, a database, a browser, a payment API), reads the results, and keeps going until a goal is met or it stops. That separates it from a chatbot, which only answers, and from a *workflow*, where a programmer fixed the steps in advance [S001]. How much an agent does without asking is a design choice, not a property of the model. The same model can be set up to ask before every action or to act and merely report [S002].

**The twelve findings that matter most**
- v1.1 revised or added findings 1, 6, 8, 10 and 11 after the limitations follow-up (§14 and `research/limitations-resolution.md`).
- v1.2 corrected finding 11 from the current Latvian legal text and added finding 12.

1. **Adoption is real but uneven and concentrated.** Gartner's 2026 CIO survey found that only 17% of organizations had deployed AI agents (sample size not published) [S098]. In McKinsey's 2026 global survey (1,719 respondents, 97 countries, May–June 2026), 40% of respondents at companies with more than $1bn revenue said their organization was "scaling" agents, against 22% at smaller firms [S084]. Across the EU, Eurostat's official survey found 20.0% of enterprises with 10+ employees used any AI technology in 2025 (Latvia: 12.2%) [S096]. That is broader than agents and still a minority. These numbers measure different things (§2.2). The most mature, best-evidenced use is **software coding**. Among developers who use AI, 66% use coding agents [S062]. Anthropic disclosed that Claude Code alone passed a $2.5bn revenue run rate in February 2026 [S141].

2. **Capability is rising fast, but reliability on real work is still low.** On paid freelance projects judged by humans, the best agent produced work as good as a professional's 15.8% of the time in July 2026. Eight months earlier the figure was 2.5% [S037]. Benchmarks of self-contained software tasks still show exponential growth [S008]. Controlled studies of developer productivity are inconclusive [S070]. **INTERPRETATION:** agents are dependable for narrow, checkable tasks, and supervision remains the norm for open-ended ones.

3. **Security is the binding constraint, and it is not solved.** OpenAI says prompt injection is "unlikely to ever be fully solved" [S118][S069]. Prompt injection means hostile instructions hidden in content the agent reads. Anthropic's own browser-agent tests cut attack success from 23.6% to 11.2%, not to zero [S068]. Documented incidents include an agent deleting a production database during a code freeze [S012], and tens of thousands of internet-exposed personal-agent installations plus hundreds of malicious add-ons [S013][S014]. The core design rule: never give one agent private data, untrusted input *and* the ability to send data out [S011].

4. **In business deployments, people, not tokens, are usually the biggest cost.** In our base model of a support agent handling 50,000 conversations a month, model usage is about **8%** of total cost. Human handling of the conversations the agent cannot resolve is about **74%**, and engineering, infrastructure and security about **17%** (**CALCULATION**, §6). The share of cases the agent fully resolves is the dominant lever. Moving it from 70% to 20% (all else equal) cuts the saving against an all-human team from 52% to 3%. In our pessimistic case the deployment costs 24% *more* than humans alone. Prompt caching roughly halves token cost and is the cheapest lever (**CALCULATION**). The exception is heavy individual or developer use with no human in the loop, where long agent runs make token bills dominant. Our heavy personal case costs about $4,600 a month (§6.4).

5. **Agents reach the world through tools, and the plumbing is standardising quickly.** The Model Context Protocol (MCP) is now the default way to connect agents to tools. It moved to a neutral Linux Foundation home with more than 10,000 published servers [S034], and shipped a major breaking revision on 28 July 2026 [S032]. Agent-to-agent communication (A2A) reached v1.0 [S035][S036]. Commerce and payment protocols (ACP, UCP, AP2, MPP, x402, Visa TAP, Mastercard Agent Pay) are **implemented but early**. Several compete (§8).

6. **"Agentic commerce" is mostly discovery today, and verified autonomous buying is tiny.** OpenAI scaled back in-chat checkout in March 2026 to focus on product discovery [S025]. AI-referred traffic to US retailers grew 138% year on year in May 2026 and converts better than other traffic. The source does not say this includes agents buying [S116]. Card networks announce "first live agentic transactions" without volumes; Visa reported "hundreds" of controlled ones [S021][S022].
   - **Best verified figure for autonomous machine payments:** on the x402 payment rail, Visa's own analysis found about **$15.0M** of adjusted volume from May 2025 to April 2026 [S091].
   - **How much of that is agents:** an independent analysis classed only **0.6%–7.5%** of screened x402 commerce as plausibly agent-driven, roughly **$5,000–11,000 a month** [S090].
   - **Global value:** no public source supports a global value for purchases agents complete without human approval (§9.2).

7. **There is no stable "agent buying preference" to optimise for.** Controlled experiments show that AI shoppers have strong position and first-offer biases. They penalise "sponsored" labels, and their preferences shift when the model is updated [S029][S030]. Agents can be talked into bad deals [S039]. People represented by a weaker agent got measurably worse prices and did not notice [S040].

8. **Platforms decide what agents may do, and they enforce it, but no one publishes an agent ban *rate*.** Amazon blocked Meta's shopping agent in September 2026 under its Conditions of Use [S063]. That came weeks after a US appeals court found Amazon unlikely to win anti-hacking claims against Perplexity's user-directed agent. Contract claims remain open [S015]. AI providers restrict using consumer subscriptions to power third-party agents, and some users report suspensions [S016][S075]. Anthropic's transparency report shows 11.4 million accounts banned in January–June 2026, all policy reasons combined. Of the 398,000 appeals, 10.6% were overturned [S094]. No platform publishes how many of its users run agents, so **no defensible agent ban rate exists in public data** (§11.3). Cloudflare announced that from 15 September 2026 "agent" bots are blocked by default on new sites' ad-supported pages [S019]. **INTERPRETATION:** being technically able to reach a site is not the same as being permitted to, and building on someone else's platform carries real risk of being cut off.

9. **Regulation is arriving in layers.** In the EU, AI systems that interact with people must disclose that they are AI from 2 August 2026, and agents are included [S074]. The heavier "high-risk" obligations were pushed to 2 December 2027 [S107]. The US relies on voluntary standards work, with no final agent standard yet [S050]. Six national cyber agencies jointly advise restrictive access controls [S051]. Singapore published the first dedicated agentic-AI governance framework [S052].

10. **Market-size forecasts are weak evidence, and they disagree by an order of magnitude depending on definition.**
    - Gartner's own table puts "AI agents and assistants" at **$29.2bn** of 2026 spending, out of $2.67trn total AI spending [S082]. Separately, Gartner projects **$985bn** of "agentic AI software spend" by 2030, a far broader concept [S083].
    - Analysts' 2030 forecasts for "the AI agents market" cluster around $50bn, but their 2025 baselines disagree by more than two to one [S056].
    - McKinsey's "$3–5 trillion agentic commerce by 2030" is a scenario. It is built from US Census data and adoption rates that McKinsey does not disclose [S086].
    - Company disclosures are firmer, though they are not GAAP revenue. Anthropic disclosed a $47bn run rate in May 2026, and one anonymous source reported $65bn by end-July [S088][S089]. Salesforce's agent product passed $1.5bn ARR on a broadened definition [S055].

11. **A Latvia-based operator can sell agent services and software worldwide, but not without friction or limits** (new §15).
    - **What works:** model and payment providers serve Latvia [S106][S104]. EU VAT rules give cross-border B2B services a reverse charge and give consumer sales a one-stop return [S099][S103].
    - **What matters most is the client mix, not the supplier mix** (corrected in v1.2 from the current Latvian text).
      - Since 1 July 2025, buying foreign AI or cloud services no longer forces full VAT registration. A special registration (s.139²) lets small operators stay below the €50,000 threshold and keep the micro-enterprise tax. The cost is 21% non-deductible VAT on those purchases and a monthly notice [S122][S124].
      - What does force full registration from the first sale is selling services to a VAT-registered business in another EU state [S122].
    - **What the operator must carry:** customer location still determines which VAT, consumer law and sanctions rules apply [S112][S113].
    - **What limits feasibility:** product type (regulated payments, high-risk AI uses) limits it more than geography does [S114][S107].
12. **For a newcomer, the credible opportunity is selling services to the people who run agents, not products that agents buy** (v1.2, §12.4 and `package/`).
    - **Where customers demonstrably pay:**
      - coding agents [S088][S062];
      - paid coding-agent training, at list prices of about €890 per person for 2 days [S128];
      - LLM security assessments, at $6k–45k+ across the market and $16k–50k+ from AI specialists [S130];
      - AI-related freelance work, up more than 22% year on year on Upwork while its total volume fell [S127].
    - **What is unproven:** independent evaluation of support agents, and anything sold *to* agents.
    - **RECOMMENDATION (conditional):** explore coding-agent enablement with measurement if the owner codes professionally. Otherwise explore small AI workflow automations, a simpler adjacent service. A limited agent risk review suits only someone with security credentials, and is not an audit or certification.
    - **Economics (CALCULATION):**
      - access to buyers matters more than the route;
      - for a newcomer without warm contacts, the first year pays about €3–11 an hour after Latvian taxes, around an average Latvian professional's net pay of about €8.7 [S126][S100];
      - with a network or strong public proof, it pays €23–36 an hour;
      - the adverse first year is a loss on every route.
    - **What would settle it:** the decisive unknown is whether buyers choose a newcomer. Only a capped test can settle that (`package/05-validation-plans.md`).

**What this means for you (RECOMMENDATIONS)**

- **Users:** start with tasks whose results you can check quickly, such as drafting, research and code with tests. Keep a human approval step for anything that sends, pays or deletes. Use the provider's official apps or API keys. Don't route consumer-subscription logins through third-party agent tools.
- **Builders:** start with the simplest design that works [S001]. Measure success per completed task, not per request. Design around the "lethal trifecta" (data + untrusted input + outbound action) [S011], and budget for evaluation and human escalation from day one.
- **Business builders (revised v1.2):** sell services to the people who run agents. After re-scoring with entry barriers (credentials, buyer access, liability, time to first revenue):
  - **coding-agent enablement with measurement** leads for owners who code;
  - **small AI workflow automations** suit owners who don't;
  - a **limited agent risk review** suits only someone with security credentials;
  - **independent support-agent evaluation** is deferred because data access and sales cycles are slow.

  All are **hypotheses**; none has been validated with customers. From Latvia, keep early clients outside the EU, or Latvian, to minimise VAT administration. Any EU VAT-registered client triggers full registration (§15). Ideas that depend on agents spending money autonomously remain the weakest-evidenced.

**Confidence.**
- **High:** definitions, protocols, prices, regulation dates, documented incidents, and the adoption figures now read from the primary survey publications.
- **Medium:** comparisons across adoption surveys, which use different definitions.
- **Low:** market-size forecasts and autonomous-agent purchase volumes. Agent activity timing now has a narrow evidence base (coding agents, chat), not a representative one.
- **Not available in public data:** agent-specific ban rates (§14).
