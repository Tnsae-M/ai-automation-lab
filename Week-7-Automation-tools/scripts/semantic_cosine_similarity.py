# A simple non-external module dependent cosine similarity checker for practicing embeddings.
import math
def cosine_similarity(v1:list[float],v2:list[float])->float:
    dot_product=sum(a*b for a,b in zip(v1,v2))
    norm_v1=math.sqrt(sum(a*a for a in v1))
    norm_v2=math.sqrt(sum(b*b for b in v2))
    result=dot_product/(norm_v1*norm_v2) if norm_v1 and norm_v2 else 0.0
    return result
if __name__=="__main__":
    # ICP Target Vector: [Tech focus, Direct-to-consumer, Scale, B2B wholesale]
    icp_vector = [0.9, 0.8, 0.7, 0.2]

    lead_tech_roaster = [0.85, 0.75, 0.8, 0.3]
    lead_local_repair = [0.1, 0.05, 0.2, 0.9]

    score_match = cosine_similarity(icp_vector, lead_tech_roaster)
    score_mismatch = cosine_similarity(icp_vector, lead_local_repair)

    print(f"Lead Match Score (Coffee Roaster): {score_match:.4f}")
    print(f"Lead Mismatch Score (Auto Repair): {score_mismatch:.4f}")
