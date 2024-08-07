import styled from 'styled-components'

import Typography from '@l3-lib/ui-core/dist/Typography'
import Tags from '@l3-lib/ui-core/dist/Tags'

import TypographySecondary from 'components/Typography/Secondary'
import { textSlicer } from 'utils/textSlicer'

type TagsRowProps = {
  items: string[]
  title: string
}

const TagsRow = ({ items, title }: TagsRowProps) => {
  return (
    <StyledRow>
      <TypographySecondary value={title} type={Typography.types.LABEL} size={Typography.sizes.sm} />

      <StyledContainer>
        {items.map((item: string, index: number) => {
          const { shortText: shortName } = textSlicer(item, 35)
          return (
            <Tags
              key={index}
              label={
                <TypographySecondary
                  value={shortName}
                  type={Typography.types.LABEL}
                  size={Typography.sizes.xss}
                />
              }
              color='Tags.colors.gradient_dark_blue'
              readOnly
              size='small'
              outlined
            />
          )
        })}
      </StyledContainer>
    </StyledRow>
  )
}

export default TagsRow

const StyledRow = styled.div`
  display: flex;
  flex-direction: column;
  gap: 5px;
`
const StyledContainer = styled.div`
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
`
