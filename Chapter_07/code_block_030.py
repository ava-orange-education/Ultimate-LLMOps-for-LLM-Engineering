# Custom training loop with distillation loss
def distillation_loss(student_logits, teacher_logits, labels, temperature=2.0):
    soft_targets = F.softmax(teacher_logits / temperature, dim=-1)
    soft_prob = F.log_softmax(student_logits / temperature, dim=-1)
    distillation_loss = F.kl_div(soft_prob, soft_targets, reduction='batchmean')
    student_loss = F.cross_entropy(student_logits, labels)
    return 0.5 * distillation_loss + 0.5 * student_loss